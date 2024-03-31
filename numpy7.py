import numpy as np

##### Reoganization Array !!!!!!!

before = np.array([[1,2,3,4],[5,6,7,8]])

print(before.reshape((2,2,2)))
print(before.reshape((8,1)))

# Vertically stacking Vectore

v1 = np.array([1,2,3,4])
v2 = np.array([5,6,7,8])

print(np.vstack([v1,v2]))
print(np.vstack([v1,v2,v2,v1]))

# Horizzontal stacking vectore

h1 = np.ones((2,4))
h2 = np.zeros((2,4))

print(np.hstack([h1,h2]))
print(np.hstack([h1,h2,h2,h1]))