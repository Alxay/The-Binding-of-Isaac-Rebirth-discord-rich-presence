"""
Design tokens for the installer UI.

Palette is a deliberate "basement at 3am" mood -- warm near-black backgrounds,
a single blood-red accent, bone/cream text -- rather than the default
customtkinter blue theme, so the tool reads as belonging to this specific mod
instead of a generic Tk utility.
"""

# --- Color palette --------------------------------------------------------
BG = "#161011"           # window background -- warm near-black
SURFACE = "#211a1b"       # card / input surface
SURFACE_ALT = "#2a2122"   # slightly raised surface (hover states)
BORDER = "#3a2d2e"        # hairline borders on cards/inputs

TEXT_PRIMARY = "#eee3d3"     # bone / candlelight white
TEXT_SECONDARY = "#a8968a"   # muted parchment
TEXT_MUTED = "#786964"       # dim caption text

BLOOD = "#a5312a"          # primary accent
BLOOD_HOVER = "#c23f35"     # accent hover (brighter)
BLOOD_DARK = "#6e211c"      # accent pressed / border

MOSS = "#5c8a3a"           # success (heart / consumable green)
MOSS_HOVER = "#6ea346"

GOLD = "#c9a227"           # warning / coin gold

ERROR = "#c0392b"

# --- Typography -------------------------------------------------------------
FONT_DISPLAY = "Georgia"          # moody serif for the hero title
FONT_BODY = "Segoe UI"            # clean, widely available UI face
FONT_MONO = "Consolas"            # paths / commands

SIZE_EYEBROW = 12
SIZE_TITLE = 25
SIZE_BODY = 13
SIZE_SMALL = 11
SIZE_BUTTON = 14

# --- Layout -----------------------------------------------------------------
RADIUS = 10
RADIUS_SM = 6
PAD_X = 36
PAD_Y = 28