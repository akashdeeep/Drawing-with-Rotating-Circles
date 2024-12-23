import numpy as np
from svgpathtools import svg2paths
import matplotlib.pyplot as plt
from scipy.spatial import cKDTree


def trim_points(points, n):
    """
    Trims the list of points to n points, evenly spread out.

    Args:
        points (list): List of (x, y) points.
        n (int): Number of points to retain.

    Returns:
        list: List of n evenly spread (x, y) points.
    """
    if n >= len(points):
        return points  # If n is greater than or equal to the total points, return all points

    step = len(points) / n  # Step size to evenly sample n points
    trimmed_points = [
        points[int(i * step)] for i in range(n)
    ]  # Pick points at regular intervals

    return trimmed_points


def sample_svg_points(svg_file, step=0.005):
    """
    Reads an SVG file and samples points along its paths in a circular manner using KD-Tree.

    Args:
        svg_file (str): Path to the SVG file.
        step (float): Step size for sampling points along the paths.

    Returns:
        list: List of sampled (x, y) points in circular order.
    """
    paths, _ = svg2paths(svg_file)  # Extract paths from SVG
    points = []

    # Sample points from the SVG paths
    for path in paths:
        length = path.length()  # Total length of the path
        num_samples = int(length / step) + 1  # Number of points to sample

        # Sample points along the path
        for i in range(num_samples):
            point = path.point(i / num_samples)
            x, y = point.real, point.imag
            points.append((x, y))

    points = trim_points(points, 2500)
    points = np.array(points)  # Convert to NumPy array for KD-Tree
    # print(len(points))
    tree = cKDTree(points)  # Build a KD-Tree for fast nearest neighbor search

    # Start with the first point
    current_index = 0
    circular_points = [points[current_index]]
    visited = set([current_index])  # Track visited points

    # Traverse points in circular order
    for _ in range(len(points) - 1):
        _, next_index = tree.query(points[current_index], k=len(points), p=2)
        for idx in next_index:
            if idx not in visited:
                visited.add(idx)
                current_index = idx
                circular_points.append(points[current_index])
                break

    return circular_points


# Usage example:
# svg_file = "icons8-homer-simpson-500.svg"  # Replace with your SVG file path
# points = sample_svg_points(svg_file, step=0.01)


# points = trim_points(points, 50000)  # Trim the points to 1000


# print(len(points))  # Number of points sampled

# print(points[:5])  # First 5 points


# # Visualize the points
# x, y = zip(*points)
# plt.plot(x, y, marker="o", markersize=1, linestyle="-")
# plt.gca().set_aspect("equal", adjustable="box")
# plt.title("SVG Path Tracing")
# plt.show()


def get_points(num_points, svg_file):
    points = sample_svg_points(svg_file, step=0.01)
    points = trim_points(points, num_points)
    return points


# print(len(get_points(1000, "icons8-homer-simpson-500.svg")))

__all__ = ["get_points"]
