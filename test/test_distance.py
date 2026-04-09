import pytest

from mypackage.utils import distance
from mypackage.geometry import Point


def test_distance():
    p1 = Point(2, 3)
    p2 = Point(3, 4)
    assert distance(p1, p2) == pytest.approx(1.41421, abs=1e-5)
