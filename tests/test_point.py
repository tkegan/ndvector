# -*- encoding: utf-8 -*-

# import from our module
from ndvector import Point, Vector

# Import from third party libraries
import pytest


def test_point_creation_from_single_scalar():
    p = Point(1.0)
    assert p.dimension == 1
    assert '1.0' == str(p)
    assert 'Point ‹Dimension: 1 Components: 1.0›' == repr(p)


def test_point_creation_from_multiple_scalars():
    p = Point(1.0, 2.0)
    assert p.dimension == 2
    assert '1.0, 2.0' == str(p)
    assert 'Point ‹Dimension: 2 Components: 1.0, 2.0›' == repr(p)


def test_print_creation_from_tuple():
    t = (2.0, 3.0)
    p = Point(t)
    assert p.dimension == 2
    assert '2.0, 3.0' == str(p)
    assert 'Point ‹Dimension: 2 Components: 2.0, 3.0›' == repr(p)


def test_point_creation_from_list():
    l = [4.0, 5.5]
    p = Point(l)
    assert p.dimension == 2
    assert '4.0, 5.5' == str(p)
    assert 'Point ‹Dimension: 2 Components: 4.0, 5.5›' == repr(p)


def test_illegal_attempt_to_set_dimension():
    p = Point(1.0)
    with pytest.raises(NotImplementedError):
        p.dimension = 3


def test_equality():
    p1 = Point(1.0)
    p2 = Point(1.0, 1.0)
    p3 = Point(-1.0, 1.0)
    p4 = Point(1.0, 1.0)
    assert p1 != p2
    assert p2 != p3
    assert p2 == p4


def test_addition_of_vector():
    p1 = Point(1.0, 0.0)
    p2 = Point(1.0, 1.0)
    v = Vector(0.0, 1.0)
    p3 = p1 + v
    assert p3 == p2


def test_subtraction_of_a_point():
    p1 = Point(1.0, 1.0)
    p2 = Point(0.0, 0.0)
    v = p1 - p2
    assert v.dimension == 2
    assert '-1.0, -1.0' == str(v)
    assert 'Vector ‹Dimension: 2 Components: -1.0, -1.0›' == repr(v)
