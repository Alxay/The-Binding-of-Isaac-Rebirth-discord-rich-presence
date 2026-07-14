"""
The Binding of Isaac -- Discord Rich Presence Installer
=========================================================

A small, self-contained GUI that downloads the latest release of the
Discord RPC mod from GitHub and drops it into the game's `mods` folder.

Run directly:
    python app.py

Build a standalone .exe:
    pip install -r requirements.txt pyinstaller
    pyinstaller build.spec

Repository this installer is built for is configured in core.py
(GITHUB_OWNER / GITHUB_REPO) -- change those two constants if you fork
this installer for a different mod.
"""
from __future__ import annotations

import os
import sys
import threading
import webbrowser
from typing import Callable, Optional

import customtkinter as ctk
from PIL import Image

import core
import theme

APP_VERSION = "1.0.0"


def resource_path(relative: str) -> str:
    """Resolve a bundled asset path, working both from source and from a
    PyInstaller-frozen executable."""
    base = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base, relative)


class ModInstaller(ctk.CTk):
    def __init__(self):
        super().__init__()

        ctk.set_appearance_mode("dark")

        self.title("Isaac RPC Installer")
        self.geometry("640x520")
        self.minsize(640, 520)
        self.configure(fg_color=theme.BG)
        self._set_window_icon()

        self.target_dir = ""
        self._install_running = False

        self._build_ui()

    # ------------------------------------------------------------------ #
    # UI construction
    # ------------------------------------------------------------------ #
    def _set_window_icon(self) -> None:
        # .ico works on Windows; other platforms fall back to a PNG photo icon.
        # Icon is purely cosmetic, so any failure here is swallowed on purpose.
        try:
            self.iconbitmap(resource_path("assets/icon.ico"))
            return
        except Exception:
            pass
        try:
            import tkinter as tk
            self._icon_photo = tk.PhotoImage(file=resource_path("assets/icon.png"))
            self.iconphoto(True, self._icon_photo)
        except Exception:
            pass

    def _build_ui(self) -> None:
        container = ctk.CTkFrame(self, fg_color="transparent")
        container.pack(fill="both", expand=True, padx=theme.PAD_X, pady=theme.PAD_Y)

        self._build_header(container)
        self._build_path_card(container)
        self._build_action_card(container)
        self._build_footer(container)

    def _build_header(self, parent) -> None:
        header = ctk.CTkFrame(parent, fg_color="transparent")
        header.pack(fill="x", pady=(0, 24))

        try:
            logo_img = ctk.CTkImage(
                light_image=Image.open(resource_path("assets/icon.png")),
                dark_image=Image.open(resource_path("assets/icon.png")),
                size=(44, 44),
            )
            ctk.CTkLabel(header, image=logo_img, text="").pack(pady=(0, 8))
        except Exception:
            pass  # missing asset shouldn't crash the app

        ctk.CTkLabel(
            header,
            text="T H E   B I N D I N G   O F   I S A A C",
            font=ctk.CTkFont(family=theme.FONT_BODY, size=theme.SIZE_EYEBROW, weight="bold"),
            text_color=theme.TEXT_SECONDARY,
        ).pack()

        ctk.CTkLabel(
            header,
            text="Discord Rich Presence Installer",
            font=ctk.CTkFont(family=theme.FONT_DISPLAY, size=theme.SIZE_TITLE, weight="bold"),
            text_color=theme.TEXT_PRIMARY,
        ).pack(pady=(2, 14))

        ctk.CTkFrame(header, fg_color=theme.BLOOD, height=2, width=64).pack()

    def _build_path_card(self, parent) -> None:
        card = ctk.CTkFrame(parent, fg_color=theme.SURFACE, corner_radius=theme.RADIUS,
                             border_width=1, border_color=theme.BORDER)
        card.pack(fill="x", pady=(0, 16))
        inner = ctk.CTkFrame(card, fg_color="transparent")
        inner.pack(fill="x", padx=20, pady=18)

        ctk.CTkLabel(
            inner, text="1. Select game folder",
            font=ctk.CTkFont(family=theme.FONT_BODY, size=theme.SIZE_BODY, weight="bold"),
            text_color=theme.TEXT_PRIMARY,
        ).pack(anchor="w")
        ctk.CTkLabel(
            inner,
            text="Main game folder (with isaac-ng.exe) or directly the 'mods' folder.",
            font=ctk.CTkFont(family=theme.FONT_BODY, size=theme.SIZE_SMALL),
            text_color=theme.TEXT_MUTED,
        ).pack(anchor="w", pady=(2, 12))

        row = ctk.CTkFrame(inner, fg_color="transparent")
        row.pack(fill="x")

        self.path_entry = ctk.CTkEntry(
            row, height=38, corner_radius=theme.RADIUS_SM,
            fg_color=theme.SURFACE_ALT, border_color=theme.BORDER, border_width=1,
            text_color=theme.TEXT_PRIMARY,
            placeholder_text="No folder selected...",
            font=ctk.CTkFont(family=theme.FONT_MONO, size=theme.SIZE_SMALL),
        )
        self.path_entry.pack(side="left", fill="x", expand=True, padx=(0, 10))
        self.path_entry.configure(state="disabled")

        self.select_btn = ctk.CTkButton(
            row, text="Browse...", width=110, height=38, corner_radius=theme.RADIUS_SM,
            fg_color=theme.SURFACE_ALT, hover_color=theme.BORDER,
            text_color=theme.TEXT_PRIMARY, border_width=1, border_color=theme.BORDER,
            font=ctk.CTkFont(family=theme.FONT_BODY, size=theme.SIZE_SMALL, weight="bold"),
            command=self.select_folder,
        )
        self.select_btn.pack(side="right")

    def _build_action_card(self, parent) -> None:
        card = ctk.CTkFrame(parent, fg_color=theme.SURFACE, corner_radius=theme.RADIUS,
                             border_width=1, border_color=theme.BORDER)
        card.pack(fill="x", pady=(0, 16))
        inner = ctk.CTkFrame(card, fg_color="transparent")
        inner.pack(fill="x", padx=20, pady=18)

        ctk.CTkLabel(
            inner, text="2. Download and install",
            font=ctk.CTkFont(family=theme.FONT_BODY, size=theme.SIZE_BODY, weight="bold"),
            text_color=theme.TEXT_PRIMARY,
        ).pack(anchor="w", pady=(0, 12))

        self.install_btn = ctk.CTkButton(
            inner, text="Download and Install", height=46, corner_radius=theme.RADIUS_SM,
            font=ctk.CTkFont(family=theme.FONT_BODY, size=theme.SIZE_BUTTON, weight="bold"),
            fg_color=theme.BLOOD, hover_color=theme.BLOOD_HOVER, text_color=theme.TEXT_PRIMARY,
            state="disabled", command=self.start_install_process,
        )
        self.install_btn.pack(fill="x", pady=(0, 14))

        self.progress_bar = ctk.CTkProgressBar(
            inner, height=8, corner_radius=4,
            fg_color=theme.SURFACE_ALT, progress_color=theme.BLOOD,
        )
        self.progress_bar.set(0)

        status_row = ctk.CTkFrame(inner, fg_color="transparent")
        status_row.pack(fill="x")
        self.status_row = status_row

        self.status_dot = ctk.CTkLabel(
            status_row, text="●", text_color=theme.TEXT_MUTED,
            font=ctk.CTkFont(size=theme.SIZE_BODY),
        )
        self.status_dot.pack(side="left", padx=(0, 6))

        self.status_label = ctk.CTkLabel(
            status_row, text="Waiting for folder selection...",
            font=ctk.CTkFont(family=theme.FONT_BODY, size=theme.SIZE_SMALL),
            text_color=theme.TEXT_MUTED, anchor="w",
        )
        self.status_label.pack(side="left", fill="x", expand=True)

        self.progress_pct = ctk.CTkLabel(
            status_row, text="", font=ctk.CTkFont(family=theme.FONT_MONO, size=theme.SIZE_SMALL),
            text_color=theme.TEXT_MUTED,
        )
        self.progress_pct.pack(side="right")

    def _build_footer(self, parent) -> None:
        footer = ctk.CTkFrame(parent, fg_color="transparent")
        footer.pack(fill="x", side="bottom", pady=(6, 0))

        link = ctk.CTkLabel(
            footer, text=f"{core.GITHUB_OWNER}/{core.GITHUB_REPO}",
            font=ctk.CTkFont(family=theme.FONT_BODY, size=theme.SIZE_SMALL, underline=True),
            text_color=theme.TEXT_SECONDARY, cursor="hand2",
        )
        link.pack(side="left")
        link.bind("<Button-1>", lambda _e: webbrowser.open(core.REPO_URL))

        ctk.CTkLabel(
            footer, text=f"Installer v{APP_VERSION}",
            font=ctk.CTkFont(family=theme.FONT_BODY, size=theme.SIZE_SMALL),
            text_color=theme.TEXT_MUTED,
        ).pack(side="right")

    # ------------------------------------------------------------------ #
    # Status helpers
    # ------------------------------------------------------------------ #
    def set_status(self, text: str, color: str = theme.TEXT_MUTED, dot: Optional[str] = None) -> None:
        self.status_label.configure(text=text, text_color=color)
        self.status_dot.configure(text_color=dot or color)

    # ------------------------------------------------------------------ #
    # Folder selection
    # ------------------------------------------------------------------ #
    def select_folder(self) -> None:
        from tkinter import filedialog

        selected_path = filedialog.askdirectory(title="Select The Binding of Isaac game folder")
        if not selected_path:
            return

        self.target_dir = selected_path
        self.path_entry.configure(state="normal")
        self.path_entry.delete(0, "end")
        self.path_entry.insert(0, selected_path)
        self.path_entry.configure(state="disabled")

        self.install_btn.configure(state="normal")
        self.set_status("Folder selected. Ready to install.", theme.TEXT_PRIMARY, theme.MOSS)

    # ------------------------------------------------------------------ #
    # Install flow
    # ------------------------------------------------------------------ #
    def start_install_process(self) -> None:
        if self._install_running:
            return
        self._install_running = True

        self.install_btn.configure(state="disabled")
        self.select_btn.configure(state="disabled")

        self.progress_bar.set(0)
        self.progress_bar.pack(fill="x", pady=(0, 10), before=self.status_row)
        self.progress_pct.configure(text="0%")
        self.set_status("Checking for latest version...", theme.GOLD, theme.GOLD)

        threading.Thread(target=self._install_thread, daemon=True).start()

    def _install_thread(self) -> None:
        try:
            mods_dir = core.resolve_mods_dir(self.target_dir)

            release = core.get_latest_release()
            installed_version = core.read_installed_version(mods_dir)

            if installed_version == release.tag_name:
                if not self._confirm_on_main_thread(
                    "Current version",
                    f"You already have the latest version ({release.tag_name}) installed.\n"
                    "Do you want to reinstall?",
                ):
                    self.after(0, self._reset_after_cancel)
                    return

            self.after(0, lambda: self.set_status(
                f"Downloading {release.asset_name}...", theme.GOLD, theme.GOLD))

            def on_progress(fraction: float) -> None:
                self.after(0, lambda: self._update_progress(fraction))

            zip_bytes = core.download_zip(release.zip_url, on_progress)

            self.after(0, lambda: self.set_status("Extracting files...", theme.GOLD, theme.GOLD))
            core.safe_extract(zip_bytes, mods_dir)
            core.write_installed_version(mods_dir, release.tag_name)

            exe_path = core.find_file(mods_dir, core.MOD_LAUNCHER_NAME)
            if not exe_path:
                raise core.InstallError(
                    f"Installation completed, but could not find '{core.MOD_LAUNCHER_NAME}' "
                    "in the downloaded archive."
                )

            self.after(0, lambda: self.finish_installation(True, exe_path))

        except core.InstallError as exc:
            self.after(0, lambda: self.finish_installation(False, str(exc)))
        except Exception as exc:  # noqa: BLE001 -- last-resort safety net for a GUI app
            self.after(0, lambda: self.finish_installation(False, f"Unexpected error: {exc}"))

    def _confirm_on_main_thread(self, title: str, message: str) -> bool:
        """Block the worker thread until the user answers a themed Yes/No
        dialog shown on the Tk main thread."""
        result_holder: dict[str, bool] = {}
        done = threading.Event()

        def show() -> None:
            self.show_confirm_dialog(
                title, message,
                on_result=lambda answer: (result_holder.__setitem__("value", answer), done.set()),
            )

        self.after(0, show)
        done.wait()
        return result_holder.get("value", False)

    def _update_progress(self, fraction: float) -> None:
        self.progress_bar.set(fraction)
        self.progress_pct.configure(text=f"{int(fraction * 100)}%")

    def _reset_after_cancel(self) -> None:
        self._install_running = False
        self.progress_bar.pack_forget()
        self.select_btn.configure(state="normal")
        self.install_btn.configure(state="normal")
        self.set_status("Installation cancelled.", theme.TEXT_MUTED, theme.TEXT_MUTED)

    def finish_installation(self, success: bool, result_data: str) -> None:
        self._install_running = False
        self.progress_bar.pack_forget()
        self.select_btn.configure(state="normal")
        self.install_btn.configure(state="normal")

        if success:
            self.set_status("Installation completed successfully!", theme.MOSS, theme.MOSS)
            self.show_success_dialog(result_data)
        else:
            self.set_status("Installation failed.", theme.ERROR, theme.ERROR)
            self.show_error_dialog("Installation Error", result_data)

    # ------------------------------------------------------------------ #
    # Themed modal dialogs (replace default tkinter messageboxes so the
    # whole app stays visually consistent)
    # ------------------------------------------------------------------ #
    def _new_dialog(self, title: str, width: int = 440, height: int = 220) -> ctk.CTkToplevel:
        dialog = ctk.CTkToplevel(self)
        dialog.title(title)
        dialog.geometry(f"{width}x{height}")
        dialog.resizable(False, False)
        dialog.configure(fg_color=theme.BG)
        dialog.transient(self)
        dialog.attributes("-topmost", True)
        dialog.after(50, dialog.grab_set)  # slight delay avoids a Tk race on some platforms
        return dialog

    def show_error_dialog(self, title: str, message: str) -> None:
        dialog = self._new_dialog(title, height=230)
        body = ctk.CTkFrame(dialog, fg_color="transparent")
        body.pack(fill="both", expand=True, padx=24, pady=22)

        ctk.CTkLabel(body, text="✕  " + title, font=ctk.CTkFont(family=theme.FONT_BODY, size=16, weight="bold"),
                     text_color=theme.ERROR).pack(anchor="w")
        ctk.CTkLabel(body, text=message, font=ctk.CTkFont(family=theme.FONT_BODY, size=theme.SIZE_BODY),
                     text_color=theme.TEXT_SECONDARY, wraplength=380, justify="left").pack(anchor="w", pady=(10, 18))

        ctk.CTkButton(body, text="Close", height=36, fg_color=theme.SURFACE_ALT, hover_color=theme.BORDER,
                      text_color=theme.TEXT_PRIMARY, corner_radius=theme.RADIUS_SM,
                      command=dialog.destroy).pack(fill="x")

    def show_confirm_dialog(self, title: str, message: str, on_result: Callable[[bool], None]) -> None:
        dialog = self._new_dialog(title, height=230)

        def respond(value: bool) -> None:
            dialog.destroy()
            on_result(value)

        dialog.protocol("WM_DELETE_WINDOW", lambda: respond(False))

        body = ctk.CTkFrame(dialog, fg_color="transparent")
        body.pack(fill="both", expand=True, padx=24, pady=22)

        ctk.CTkLabel(body, text=title, font=ctk.CTkFont(family=theme.FONT_BODY, size=16, weight="bold"),
                     text_color=theme.TEXT_PRIMARY).pack(anchor="w")
        ctk.CTkLabel(body, text=message, font=ctk.CTkFont(family=theme.FONT_BODY, size=theme.SIZE_BODY),
                     text_color=theme.TEXT_SECONDARY, wraplength=380, justify="left").pack(anchor="w", pady=(10, 18))

        btn_row = ctk.CTkFrame(body, fg_color="transparent")
        btn_row.pack(fill="x")
        ctk.CTkButton(btn_row, text="Cancel", height=36, fg_color=theme.SURFACE_ALT, hover_color=theme.BORDER,
                      text_color=theme.TEXT_PRIMARY, corner_radius=theme.RADIUS_SM,
                      command=lambda: respond(False)).pack(side="left", fill="x", expand=True, padx=(0, 8))
        ctk.CTkButton(btn_row, text="Reinstall", height=36, fg_color=theme.BLOOD,
                      hover_color=theme.BLOOD_HOVER, text_color=theme.TEXT_PRIMARY, corner_radius=theme.RADIUS_SM,
                      command=lambda: respond(True)).pack(side="right", fill="x", expand=True)

    def show_success_dialog(self, exe_path: str) -> None:
        cmd = f'"{os.path.normpath(exe_path)}" %command%'

        dialog = self._new_dialog("Success!", width=560, height=290)
        body = ctk.CTkFrame(dialog, fg_color="transparent")
        body.pack(fill="both", expand=True, padx=26, pady=24)

        ctk.CTkLabel(body, text="✓  Installation completed!",
                     font=ctk.CTkFont(family=theme.FONT_BODY, size=17, weight="bold"),
                     text_color=theme.MOSS).pack(anchor="w")
        ctk.CTkLabel(body, text="Copy the following text and paste it into the Steam launch options of the game:",
                     font=ctk.CTkFont(family=theme.FONT_BODY, size=theme.SIZE_BODY),
                     text_color=theme.TEXT_SECONDARY, wraplength=480, justify="left").pack(anchor="w", pady=(8, 14))

        entry = ctk.CTkEntry(body, height=38, corner_radius=theme.RADIUS_SM, fg_color=theme.SURFACE,
                              border_color=theme.BORDER, border_width=1, text_color=theme.TEXT_PRIMARY,
                              font=ctk.CTkFont(family=theme.FONT_MONO, size=theme.SIZE_SMALL))
        entry.pack(fill="x", pady=(0, 14))
        entry.insert(0, cmd)
        entry.configure(state="readonly")

        def copy_to_clipboard() -> None:
            dialog.clipboard_clear()
            dialog.clipboard_append(cmd)
            dialog.update()
            copy_btn.configure(text="Copied!", fg_color=theme.MOSS, hover_color=theme.MOSS_HOVER)
            dialog.after(1800, lambda: copy_btn.configure(text="Copy to clipboard", fg_color=theme.BLOOD,
                                                            hover_color=theme.BLOOD_HOVER))

        row = ctk.CTkFrame(body, fg_color="transparent")
        row.pack(fill="x")
        copy_btn = ctk.CTkButton(row, text="Copy to clipboard", height=38, corner_radius=theme.RADIUS_SM,
                                  fg_color=theme.BLOOD, hover_color=theme.BLOOD_HOVER,
                                  text_color=theme.TEXT_PRIMARY, command=copy_to_clipboard)
        copy_btn.pack(side="left", fill="x", expand=True, padx=(0, 8))
        ctk.CTkButton(row, text="Close", height=38, corner_radius=theme.RADIUS_SM, fg_color=theme.SURFACE_ALT,
                      hover_color=theme.BORDER, text_color=theme.TEXT_PRIMARY,
                      command=dialog.destroy).pack(side="right", fill="x", expand=True)


def main() -> None:
    app = ModInstaller()
    app.mainloop()


if __name__ == "__main__":
    main()