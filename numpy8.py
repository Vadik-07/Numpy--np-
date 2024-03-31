import numpy as np

####  Miscellaneous !!!!

# Load Data From Files

file_data = np.genfromtxt('data.txt', delimiter=',')
file_data = file_data.astype('int32')
print(file_data)

###### Boolean Masking and Advance Indexing !!!!!!!!

print(file_data > 50)
print(file_data[file_data > 50])

# You can Index with a list in NumPy

a = np.array([1,2,3,4,5,6,7,8,9])
print(a[[1,2,8]])

print((file_data > 50) & (file_data < 100))

que = np.array([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25],[26,27,28,29,30]])
print(que[ 2:4 , 0:2 ])

for i in range(0,4):      
    print(que[i,i+1])       # Output : 2,8,14,20

print(que[[0,1,2,3],[1,2,3,4]])    # Output : 2,8,14,20

print(que[[0,0,4,4,5,5],[3,4,3,4,3,4]])  # Output : 4,5,24,25,29,30
# Another Way
print(que[[0,4,5], 3:])

# To Calculate Det
arr = np.array([[-3,1],[2,1]])
print(np.linalg.det(arr))
