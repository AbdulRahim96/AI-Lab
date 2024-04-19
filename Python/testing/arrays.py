import numpy as np

mylist = [[1, 2, 3, 4, 5],
         [2, 3, 4, 5, 6],
         [3, 4, 5, 6, 7]]

arr = np.array(mylist)
arr2 = arr.reshape(15, 1)
print(arr.shape)

print(arr2)