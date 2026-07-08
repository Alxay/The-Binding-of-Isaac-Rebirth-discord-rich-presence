from pathlib import Path
import sys
import subprocess

if getattr(sys, 'frozen', False):
	base = Path(sys.executable).resolve().parent.parent
else:
	base = Path(__file__).resolve().parent

mod = (base / "main.exe").resolve()
game = (base / ".." / ".." / "isaac-ng.exe").resolve()

subprocess.Popen([str(mod)], cwd=str(mod.parent))
subprocess.Popen([str(game)], cwd=str(game.parent))