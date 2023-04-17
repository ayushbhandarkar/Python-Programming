# creating numpy array changing dimension using ndmin
import numpy as np
list = []
size = int(input(" Enter the size of array : "))
print(" Enter the array element : ")
for i in range(size):
    list.append(int(input()))

print(" List : ", list)
arr = np.array(list, ndmin=2)
print(" Numpy array : ", arr)
print(" no. of dimensions : ", arr.ndim)
