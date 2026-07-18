import math


def hex_points(center_x, center_y, size):
    points = []
    for i in range(6):
        angle_deg = 60 * i - 30  # -30 = pointy-top
        angle_rad = math.radians(angle_deg)
        x = center_x + size * math.cos(angle_rad)
        y = center_y + size * math.sin(angle_rad)
        points.append((x, y))
    return points
