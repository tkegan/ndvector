# About
*ndvector* is yet another vector math library for Python3. Where numpy focuses
on everything including the kitchen sink, ndvector is intended to provide a
simple, pythonic, object oriented API for vector math in n dimensions.

# License
Apache License 2.0 (see LICENSE)

# Requirements
python >= 3.5

# Usage
Usage attempts to be about what you expect. Simply import the library, create
Point and Vector objects, and do math with them.

```python
from n_dimension import Vector

v1 = Vector(1.0, 0.0)
v2 = Vector(-1.0, 1.0)
v3 = v1 + v2
print(v3) # => Vector ‹0.0, 1.0›
```

# API
Given:

	- s a scalar (float)

	- p, p# are instances of Point

	- v, v# are instances of Vector

Class `Point`:

	- constructor - create a Point from one or more float parameters, a tuple
		of floats, or a list of floats

	- properties:

		- dimension - the dimension of the Point

	- operators:

		- 'p + v' addition of a Vector to a Point to get the Point at the tip of
			the Vector if the tail of the vector is moved to the Point

		- 'p1 - p2' subtraction of a Point from a Point to get the Vector between
			the Points

		- 'p1 == p2' equality (See Note 1)

		- 'p1 != p2' not equality (See Note 1)

Class `Vector`:

	- constructor - create a Vector from one or more float parameters, a tuple
		of floats, or a list of floats

	- properties:
		- dimension - the dimension of the vector
		- magnitude - the magnitude of the vector

	- operators

		- 'v1 + v2' vector addition

		- 'v1 - v2' vector subtraction

		- 'v1 * v2' scalar aka dot product (v1 * v2 => scalar)

		- 'v * s' scale vector

		- 'v1 @ v2' vector aka cross product (v1 * v2 => vector) (See Note 2)

		- 'v1 == v2' equality (See Note 1)

		- 'v1 != v2' not equality (See Note 1)

	- methods

		- angle() - find the angle in radians between the vector and another vector

		- normalize() - find a unit vector with the same direction as the vector

## Notes
1) testing for equality when floats are involved is tricky. n_dimension
	considers two floats to be equal if the absolute value of their difference
	is less than a certain amount; currently 0.000001 seems to work well. This
	may be refined after more testing
2) only implemented for Vectors of dimension three (3)

# Testing
Testing is done using `tox` and `pytest`. See
https://tox.readthedocs.io/en/latest/ for information about installing tox.
Run the tests by cloning the source repository, changing into the local
working directory, and invoking `tox`.

```sh
git clone https://github.com/tkegan/n_dimension.git
cd n_dimension
tox
```

# To Do
- Create better API documentation

- Investigate accelerated performance by moving some functionality to compiled code but only if the pure python implementation can be kept as a fallback

# Contribute
I welcome pull requests against the GitHub repository. If extending the API, please include tests. I will not merge changes to the API until tests are in place and passing.
