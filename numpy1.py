import numpy as np

a = np.array([1, 2, 3])
print(a)

b = np.array([[1.0, 2.0, 3.0, 4.0], [1, 2.0, 3, 4.0], [1, 2, 3, 4], [5, 6, 7, 8]])
print(b)

# Tells Which Dimension Array is that
print(a.ndim)
print(b.ndim)

# Tells Which Shape or size of Array is that
print(a.shape)
print(b.shape)

#  Get Type wether array is  integer, float, string, etc.
print(a.dtype)
print(b.dtype)

# Get Size return the Size in Bites
print(a.itemsize)
print(b.itemsize)

# Get size
print(a.size)
print(b.size)
