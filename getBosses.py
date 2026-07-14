from __future__ import annotations

from pathlib import Path
from xml.etree import ElementTree as ET


def load_bosses(xml_path: str | Path | None = None) -> dict[int, dict[str, str]]:
	if xml_path is None:
		xml_path = Path(__file__).resolve().parents[2] / "resources-dlc3" / "bossportraits.xml"

	tree = ET.parse(xml_path)
	root = tree.getroot()

	bosses: dict[int, dict[str, str]] = {}
	for boss in root.findall("boss"):
		boss_id = int(boss.get("id"))
		bosses[boss_id] = {
			"name": boss.get("name", ""),
			"nameimage": boss.get("nameimage", ""),
		}

	return bosses


bosses = load_bosses()
print(bosses)