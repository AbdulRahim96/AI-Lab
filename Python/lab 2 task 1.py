import numpy as np

maxDimension = 8

array = np.ones((maxDimension,maxDimension)) # all 1s
array[1 : maxDimension-1 , 1 : maxDimension-1] = 0 # neglecting 1st : last rows , neglecting 1st : last columns

print(array)