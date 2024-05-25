import numpy as np

mylist = [[1, 2, 3, 4, 5],
         [2, 3, 4, 5, 6],
         [3, 4, 5, 6, 7],
         [5, 3, 1, 3, 8]]

arr = np.array(mylist)
arr2 = arr.reshape(1, 20)
print(arr.shape)

print(arr2)