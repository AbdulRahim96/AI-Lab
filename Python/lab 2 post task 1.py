import numpy as np

dimensions = 8
ar1 = np.ones((dimensions,dimensions))
#ar1[ : : 2, : : 2] = 0 # even number of rows
#ar1[1: :2, 1: :2] = 0 # odd number of rows
#print(ar1)

mylist = [1,0,0,0,0,1]

print(0 in mylist[0])