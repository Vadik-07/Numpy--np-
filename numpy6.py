import numpy as np

###### Linera Algebra !!!!!!!

a = np.ones((2,3))
b = np.full((3,2), 2)
print(a)
print(b)

# Matrix Muttipllication

print(np.matmul(a,b))

# Find the Determinant
# To calculate determent

# det([a,b]
#     [c,d]) = ad - bc

#  to claculate 3D Determent

# det([a,b,c]
#     [d,e,f]    = a det([e,f]
#     [g,h,i])          [h,i])
#                 -b det([d,f]
#                        [g,i])
#                 +c det([d,e]
#                        [g,h])

c = np.identity(3)
print(np.linalg.det(c))

m1 = np.array([[4,2],[2,1]])
print(np.linalg.det(m1))

####### Statistics !!!!!!!

stats = np.array([[1,2,3],[4,5,6]])

print(np.min(stats))
print(np.max(stats))
print(np.sum(stats))