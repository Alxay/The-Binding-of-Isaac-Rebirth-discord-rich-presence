"""
Core (non-GUI) logic for the installer: talking to the GitHub Releases API,
downloading with progress reporting, and safely extracting the archive.

Kept separate from app.py so it can be unit-tested / reused without Tk.
"""
from __future__ import annotations

import io
import json
import os
import zipfile
from dataclasses import dataclass
from typing import Callable, Optional

import requests

# ---------------------------------------------------------------------------
# Configuration -- edit these if you fork this installer for another mod.
# ---------------------------------------------------------------------------
GITHUB_OWNER = "Alxay"
GITHUB_REPO = "The-Binding-of-Isaac-Rebirth-discord-rich-presence"
GAME_EXE_NAME = "isaac-ng.exe"
MOD_LAUNCHER_NAME = "launcher.exe"
VERSION_MARKER_FILE = ".installed_version.json"

API_URL = f"https://api.github.com/repos/{GITHUB_OWNER}/{GITHUB_REPO}/releases/latest"
REPO_URL = f"https://github.com/{GITHUB_OWNER}/{GITHUB_REPO}"

REQUEST_TIMEOUT = 15
DOWNLOAD_TIMEOUT = 60
USER_AGENT = "isaac-discord-rpc-installer"


class InstallError(Exception):
    """Raised for any expected, user-facing installation failure."""


@dataclass
class ReleaseInfo:
    tag_name: str
    zip_url: str
    asset_name: str


def get_latest_release() -> ReleaseInfo:
    """Fetch the newest GitHub release and return the first .zip asset found."""
    try:
        resp = requests.get(
            API_URL,
            headers={"User-Agent": USER_AGENT, "Accept": "application/vnd.github+json"},
            timeout=REQUEST_TIMEOUT,
        )
    except requests.exceptions.RequestException as exc:
        raise InstallError(f"Failed to connect to GitHub: {exc}") from exc

    if resp.status_code == 403:
        raise InstallError(
            "GitHub API rejected the request (rate limit exceeded). Please try again in a moment."
        )
    if resp.status_code == 404:
        raise InstallError("Repository or release not found.")
    if not resp.ok:
        raise InstallError(f"GitHub returned HTTP error {resp.status_code}.")

    data = resp.json()
    for asset in data.get("assets", []):
        if asset.get("name", "").endswith(".zip"):
            return ReleaseInfo(
                tag_name=data.get("tag_name", "unknown"),
                zip_url=asset["browser_download_url"],
                asset_name=asset["name"],
            )

    raise InstallError("The latest release does not contain a .zip file.")


def read_installed_version(mods_dir: str) -> Optional[str]:
    marker = os.path.join(mods_dir, VERSION_MARKER_FILE)
    if not os.path.isfile(marker):
        return None
    try:
        with open(marker, "r", encoding="utf-8") as f:
            return json.load(f).get("tag_name")
    except (OSError, json.JSONDecodeError):
        return None


def write_installed_version(mods_dir: str, tag_name: str) -> None:
    marker = os.path.join(mods_dir, VERSION_MARKER_FILE)
    try:
        with open(marker, "w", encoding="utf-8") as f:
            json.dump({"tag_name": tag_name}, f)
    except OSError:
        pass  # non-critical: worst case we just re-offer the update later


def download_zip(url: str, on_progress: Callable[[float], None]) -> bytes:
    """Download a URL to memory, reporting progress in [0, 1] via on_progress."""
    try:
        with requests.get(url, stream=True, timeout=DOWNLOAD_TIMEOUT) as resp:
            resp.raise_for_status()
            total = int(resp.headers.get("Content-Length", 0))
            buf = io.BytesIO()
            downloaded = 0
            for chunk in resp.iter_content(chunk_size=65536):
                if not chunk:
                    continue
                buf.write(chunk)
                downloaded += len(chunk)
                if total > 0:
                    on_progress(min(downloaded / total, 1.0))
            return buf.getvalue()
    except requests.exceptions.RequestException as exc:
        raise InstallError(f"Error downloading file: {exc}") from exc


def _is_within_directory(directory: str, target: str) -> bool:
    directory = os.path.abspath(directory)
    target = os.path.abspath(target)
    return os.path.commonpath([directory]) == os.path.commonpath([directory, target])


def safe_extract(zip_bytes: bytes, destination: str) -> None:
    """Extract a zip archive, rejecting any entry that would escape `destination`
    (a "zip slip" path-traversal guard), while renaming the top-level folder to 'discordrichpresence'."""
    import shutil

    target_mod_folder_name = "discordrichpresence"
    target_mod_path = os.path.join(destination, target_mod_folder_name)

    with zipfile.ZipFile(io.BytesIO(zip_bytes)) as archive:
        members = archive.infolist()
        if not members:
            raise InstallError("The downloaded archive is empty.")

        # Determine if there is a common root directory in the zip
        common_root = None
        first_member = members[0].filename.replace("\\", "/")
        first_part = first_member.split("/")[0]
        if first_part:
            is_common = True
            has_dir_indicator = False
            for member in members:
                norm_name = member.filename.replace("\\", "/")
                if not (norm_name == first_part or norm_name.startswith(first_part + "/")):
                    is_common = False
                    break
                if norm_name == first_part + "/" or norm_name.startswith(first_part + "/"):
                    has_dir_indicator = True
            if is_common and has_dir_indicator:
                common_root = first_part

        # Clean up the existing destination folder if it exists, to ensure a clean install/update
        if os.path.exists(target_mod_path):
            try:
                def remove_readonly(func, path, _):
                    import stat
                    os.chmod(path, stat.S_IWRITE)
                    func(path)
                shutil.rmtree(target_mod_path, onerror=remove_readonly)
            except OSError as exc:
                raise InstallError(
                    f"Failed to remove existing mod directory '{target_mod_path}': {exc}. "
                    "Make sure the game and launcher are closed."
                ) from exc

        # Create target directory
        os.makedirs(target_mod_path, exist_ok=True)

        for member in members:
            # We rewrite the filename to map it to target_mod_folder_name
            norm_name = member.filename.replace("\\", "/")
            parts = [p for p in norm_name.split("/") if p]
            if not parts:
                continue

            if common_root:
                # Replace the first component with target_mod_folder_name
                parts[0] = target_mod_folder_name
            else:
                # Prepend target_mod_folder_name
                parts.insert(0, target_mod_folder_name)

            # Reconstruct the member filename
            new_filename = "/".join(parts)
            # If the original filename ended with a slash, preserve it
            if member.filename.endswith("/") or member.filename.endswith("\\"):
                new_filename += "/"

            member.filename = new_filename

            # Perform the path-traversal check on the new destination-based path
            member_path = os.path.join(destination, member.filename)
            if not _is_within_directory(destination, member_path):
                raise InstallError(
                    "Archive contains a suspicious file path and has been rejected "
                    "(zip slip protection)."
                )

            # Extract the member
            archive.extract(member, destination)


def find_file(root: str, filename: str) -> Optional[str]:
    for current_root, _dirs, files in os.walk(root):
        if filename in files:
            return os.path.join(current_root, filename)
    return None


def resolve_mods_dir(selected_path: str) -> str:
    """Given a user-selected folder, return the correct `mods` directory,
    creating it if needed. Raises InstallError if the game can't be located."""
    path = os.path.normpath(selected_path)
    parent_dir = os.path.dirname(path)

    # Case 1: user selected the "mods" folder directly.
    if os.path.basename(path).lower() == "mods" and os.path.isfile(
        os.path.join(parent_dir, GAME_EXE_NAME)
    ):
        return path

    # Case 2: user selected the main game folder.
    if os.path.isfile(os.path.join(path, GAME_EXE_NAME)):
        mods_dir = os.path.join(path, "mods")
        os.makedirs(mods_dir, exist_ok=True)
        return mods_dir

    raise InstallError(
        f"Could not find '{GAME_EXE_NAME}'. Make sure you selected the correct game folder."
    )