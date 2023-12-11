# Add this line at the top of your utils.py file
from __future__ import annotations


class PointTypeError(TypeError):
    """Exception raised for errors in the input type."""

    def __init__(self):
        super().__init__("p1 and p2 must be instances of Point")


def distance(p1, p2) -> float:
    from .geometry import Point

    if not isinstance(p1, Point) or not isinstance(p2, Point):
        raise PointTypeError()
    return ((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2) ** 0.5
