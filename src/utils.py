import math
import colorsys

def sin(degrees):
    return math.sin(math.radians(degrees))

def cos(degrees):
    return math.cos(math.radians(degrees))

def get_hsv_color(h, s, v):
    r, g, b = colorsys.hsv_to_rgb(h, s, v / 255.0)
    return (int(r * 255), int(g * 255), int(b * 255))