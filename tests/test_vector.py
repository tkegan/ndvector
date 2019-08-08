# -*- encoding: utf-8 -*-
#import from Python Standard Library
import math

# import from our module
from ndvector import Vector

# Import from third party libraries
import pytest


def test_vector_creation_from_single_scalar():
    v = Vector(1.0)
    assert v.dimension == 1
    assert v.magnitude == 1.0
    assert 'Vector of Dimension 1' == repr(v)
    assert 'Vector ‹1.0›' == str(v)


def test_vector_creation_from_multiple_scalars():
    v = Vector(1.0, 1.0)
    assert v.dimension == 2
    assert 0.1 > abs(v.magnitude - 1.414)
    assert 'Vector of Dimension 2' == repr(v)
    assert 'Vector ‹1.0, 1.0›' == str(v)


def test_vector_creation_from_tuple():
    t = (0.5, 1.2)
    v = Vector(t)
    assert v.dimension == 2
    assert v.magnitude == 1.3
    assert 'Vector of Dimension 2' == repr(v)
    assert 'Vector ‹0.5, 1.2›' == str(v)


def test_vector_from_list():
    l = [3.0, 4.0]
    v = Vector(l)
    assert v.dimension == 2
    assert v.magnitude == 5.0
    assert 'Vector of Dimension 2' == repr(v)
    assert 'Vector ‹3.0, 4.0›' == str(v)


def test_illegal_attempt_to_set_dimension():
    v = Vector(1.0)
    with pytest.raises(NotImplementedError):
        v.dimension = 3


def test_equality():
    v1 = Vector(1.0)
    v2 = Vector(1.0, 1.0)
    v3 = Vector(-1.0, 1.0)
    v4 = Vector(1.0, 1.0)
    assert v1 != v2
    assert v2 != v3
    assert v2 == v4


def test_addition():
    v1 = Vector(1.0, 0.0, -1.0)
    v2 = Vector(0.0, 1.0, 1.0)
    v3 = v1 + v2
    v4 = Vector(1.0, 1.0, 0.0)
    assert v3 == v4


def test_subtraction():
    v1 = Vector(1.0, 0.0, -1.0)
    v2 = Vector(0.0, 1.0, 1.0)
    v3 = v1 - v2
    v4 = Vector(1.0, -1.0, -2.0)
    assert v3 == v4


def test_multiplication_by_scalar():
    v1 = Vector(2.5, 1.2, -1.0)
    v2 = Vector(5.0, 2.4, -2.0)
    product = v1 * 2.0
    assert product == v2


def test_scalar_multiplication():
    v1 = Vector(2.5, 1.2, -1.0)
    v2 = Vector(0.0, 1.0, 1.0)
    product = v1 * v2
    assert 0.000001 > abs(product - 0.2)


def test_vector_multiplication():
    v1 = Vector(3.0, -3.0, 1.0)
    v2 = Vector(4.0, 9.0, 2.0)
    v3 = Vector(-15.0, -2.0, 39.0)
    product = v1 @ v2
    assert product == v3


def test_vector_normalization():
    v1 = Vector(8.0)
    u1 = Vector(1.0)
    u = v1.normalize()
    assert u1 == u

    v2 = Vector(3.0, -4.0)
    u2 = Vector(0.6, -0.8)
    u = v2.normalize()
    assert u2 == u


def test_angle_between_vectors():
    v1 = Vector(0.0, 0.0, 2.0)
    v2 = Vector(0.707, 1.5, 0.0)

    theta = v2.angle(v1)
    assert 0.000001 > abs(theta - (math.pi / 2.0))
