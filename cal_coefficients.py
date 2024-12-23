import math, cmath
import read_svg


def get_angular_frequencies(num_coefficients):
    """
    Get angular velocities for the given number of Fourier coefficients.

    Args:
        num_coefficients (int): Number of coefficients.

    Returns:
        list: List of angular velocities.
    """
    w = []
    cnt = 0
    while cnt < num_coefficients:
        if cnt == 0:
            cnt += 1
            w += [0]
        else:
            w += [(cnt + 1) // 2]
            cnt += 1
            if cnt < num_coefficients:
                w += [-(cnt) // 2]
                cnt += 1
    return w


def get_coefficients(points, num_coefficients):
    """
    Get Fourier coefficients for the given list of points.

    Args:
        points (list): List of (x, y) points.
        num_coefficients (int): Number of coefficients to calculate.

    Returns:
        list: List of Fourier coefficients.
    """
    coefficients = []
    N = len(points)
    w = get_angular_frequencies(num_coefficients)
    delta = 1 / N
    for n in w:
        coefficient = 0
        for i in range(N):
            x, y = points[i]
            z = complex(x, y)
            coefficient += z * delta * cmath.exp(-2j * math.pi * n * i / N)
        coefficients.append(coefficient)
    return coefficients


__all__ = ["get_coefficients", "get_angular_frequencies"]
