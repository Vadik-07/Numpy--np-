import numpy as np

a = [[1,2,3,4,5,6],[7,8,9,10,11,12]]

#  to Get all 0's Matrix
print(np.zeros((2,4)))

#  to Get all 1's Matrix
print(np.ones((2,4)))

# to Get an full Specified Number's MAtrix
print(np.full((2,7),99))

# Any other Number (full_like)
print(np.full_like(a,55))
a = np.full_like(a,22)
print(a)

# to Get a Randam Decimal Number
print(np.random.rand(2,5))
print(np.random.random_sample(a.shape))

# to Get Random Integer
print(np.random.randint(-9,9, size=(6)))

# identy Matrix 
print(np.identity(4))

# to repeat an Array
arr1 = np.array([1,2,3])
print(np.repeat(arr1,4))
arr2 = np.array([[1,2,3]]) # 2-D Array
print(np.repeat(arr2,3, axis=0))
print(np.repeat(arr2,3, axis=1))

# Question Print This using above Method

#   1 1 1 1 1
#   1 0 0 0 1
#   1 0 9 0 1
#   1 0 0 0 1
#   1 1 1 1 1

pr = np.ones((5,5))
for i in range(1,4):
    pr[i, 1:4] = 0
pr[2,2] = 9
print(pr)

# Using Replace method
output = np.zeros((5,5))
z = np.ones((3,3))
z[1,1] = 9
output[ 1:4 , 1:4 ] = z   #  output[ starting row to ending row , starting coloum to ending coloum]
print(output)