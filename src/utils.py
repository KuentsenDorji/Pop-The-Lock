import math
import colorsys
from pathlib import Path

def sin(degrees):
    return math.sin(math.radians(degrees))

def cos(degrees):
    return math.cos(math.radians(degrees))

def get_hsv_color(h, s, v):
    r, g, b = colorsys.hsv_to_rgb(h, s, v / 255.0)
    return (int(r * 255), int(g * 255), int(b * 255))

def load_sound(filename):
    base = Path(__file__).resolve().parent
    music = base.parent / "assets" / filename
    return music