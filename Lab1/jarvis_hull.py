import numpy as np


def ccw(p1, p2, p3):
    if (p3[1]-p1[1])*(p2[0]-p1[0]) >= (p2[1]-p1[1])*(p3[0]-p1[0]):
        return True
    return False


def jarvis_hull(points):
    hull = []
    hull_point = min(points, key=lambda p: (p[0], p[1]))

    while True:
        hull.append(hull_point)
        endpoint = points[0]

        for j, point in enumerate(points):
            if np.all(endpoint == hull_point) or not ccw(point, hull_point, endpoint):
                endpoint = point

        hull_point = endpoint

        if np.all(endpoint == hull[0]):
            break

    return np.array(hull)
