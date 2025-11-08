colors = {
    "Black": (0, 0, 0),
    "Silver": (192, 192, 192),
    "Gray": (128, 128, 128),
    "White": (255, 255, 255),
    "Maroon": (128, 0, 0),
    "Red": (255, 0, 0),
    "Purple": (128, 0, 128),
    "Fuchsia": (255, 0, 255),
    "Green": (0, 128, 0),
    "Lime": (0, 255, 0),
    "Olive": (128, 128, 0),
    "Yellow": (255, 255, 0),
    "Navy": (0, 0, 128),
    "Blue": (0, 0, 255),
    "Teal": (0, 128, 128),
    "Aqua": (0, 255, 255)
}

while True:
    r, g, b = map(int, input().split())
    if (r, g, b) == (-1, -1, -1):
        break
    min_dist = float('inf')
    closest = ""
    for name, (R, G, B) in colors.items():
        dist = (r - R)**2 + (g - G)**2 + (b - B)**2
        if dist < min_dist:
            min_dist = dist
            closest = name
    print(closest)
