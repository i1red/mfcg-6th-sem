import numpy as np
import matplotlib.pyplot as plt

from jarvis_hull import jarvis_hull
from bezier import bezier_approximation


def main():
    points = np.random.uniform(-100, 100, (100, 2))
    hull = jarvis_hull(points)
    closed_hull = np.append(hull, hull[:1], axis=0)

    approximation = bezier_approximation(closed_hull, 75)

    points_x, points_y = points[:, 0], points[:, 1]
    closed_hull_x, closed_hull_y = closed_hull[:, 0], closed_hull[:, 1]
    approximation_x, approximation_y = approximation[:, 0], approximation[:, 1]

    plt.plot(points_x, points_y, 'o')
    plt.plot(closed_hull_x, closed_hull_y)
    plt.plot(approximation_x, approximation_y, 'g-')
    plt.plot(closed_hull_x, closed_hull_y, 'ro')

    plt.show()


if __name__ == '__main__':
    main()