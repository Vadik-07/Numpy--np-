import numpy as np

###### Be Carefull when Copying Array!!!!!!!!!

a = np.array([1,2,3])
b = a
print(b)  # Output : [1 2 3] 
b[0] = 100
print(b)  # Output : [100 2 3]
print(a)  # Output : [100 2 3] 

# To fix that
# we can create a copy of a
aa = np.array([1,2,3])
bb = aa.copy()
print(bb)
bb[0] = 100
print(bb)
print(aa)