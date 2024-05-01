import pandas as pd

class Circle:
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return self.radius * self.radius * 3.14
    def perimeter(self):
        return 2 * self.radius * 3.14
    

evenlist = [2,4,6,8,10,12,14,16,18,20]
print("Series: ", evenlist)
# get odd indices from evenlist
oddlist = evenlist

index = 0
for i in oddlist:
    oddlist[index] = i - 1
    index = index + 1

print(oddlist)


    
# make a pandas series
series = pd.Series([1,2,3,4,5,6])

def function(ser):
    for i in ser:
        ans = i/2
        print(ans)

function(series)

#convert a binary numpy array to boolean numpy array
import numpy as np

# create array of values 1 and 0
array = np.array([1,0,1,0,1,0,1,0,1,0])
print(array)
# convert this array to boolean array
bool_array = array.astype(bool)
print(bool_array)

