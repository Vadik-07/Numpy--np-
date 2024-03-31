import numpy as np

a = np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])

# Get an Specific Element
print(a[1,6])

# Get an Specific Row
print(a[1, :])

# Get an Specific Coloum
print(a[: ,4])

# Getting a little more fancy [startingindex:endingindex:stepsize]
print(a[0, 1:6:2])

# Get Changed an Element
a[1,3] = 111
print(a)

# Create a 3D array with random values
# Syntax: np.array([[[element1, element2, ...], [element3, element4, ...]], ...])
array_3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

# Print the 3D array
print("3D Array:")
print(array_3d)

# Get the shape of the array
print("\nShape of the array:", array_3d.shape)

# Get an Specific Element in 3D array
print(array_3d[1,1,1])