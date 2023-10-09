import numpy as np
import matplotlib.pyplot as plt
from typing import Tuple


# Exercise 1
print('hello world')


def get_params_linear_function(
        point1: np.array,
        point2: np.array
) -> Tuple[float, float]:
    """Calculate slope and intercept of a linear function from 2 Points"""
    slope = (point2[1] - point1[1]) / (point2[0] - point1[0])
    intercept = point1[1] - slope * point1[0]
    intercept1 = point2[1] - slope * point2[0]
    print(f"m = {slope}, n={intercept}, n1={intercept1}")
    assert round(intercept, 5) == round(intercept1, 5), print('n and n1 are not equal')
    return slope, intercept


def plot_linear_function(
        slope: float,
        intercept: float,
        point1: np.array,
        point2: np.array
) -> None:
    """Plot a linear function"""
    x = np.linspace(-10, 10, 100)
    y = slope * x + intercept
    # plot x- and y-axis and point1 and point2
    plt.axhline(y=0, color='k')
    plt.axvline(x=0, color='k')
    plt.plot(point1[0], point1[1], 'ro')
    plt.plot(point2[0], point2[1], 'ro')
    plt.plot(x, y)

    # axis labels and title
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Linear function')

    # axis limits
    plt.xlim((-5, 5))
    plt.ylim((-10, 10))

    # grid
    plt.grid(True)

    # aspect ratio 1
    plt.gca().set_aspect('equal', adjustable='box')

    plt.show()


if __name__ == '__main__':
    pass
    # Exercise 2
    S = np.array([2, 7])
    E = np.array([-3, -8])
    slope, intercept = get_params_linear_function(S, E)
    plot_linear_function(slope, intercept, point1=S, point2=E)

    # Exercise 3

