import numpy as np
import pandas as pd

example1 = np.array([1,2,3,4,5,6])
print(example1)
print(type(example1))
#output
#[1 2 3 4 5 6]
#<class 'numpy.ndarray'>

#1-D (Array)
example2 = np.array([1,2,3,4,5,6])
#2-D (Matrix)
example2 = np.array([[1, 2, 3], [4, 5, 6]])
#3-D (Tensor)
example3 = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

#array operations
example3 = np.array([1,2,3,4,5,6])
example3[3] == 4
example3[1:] == [2,3,4,5]
#multidimensional operations
example3 = np.array([[1, 2, 3], [4, 5, 6]])
np.array(example3[1,1:3]) == [4,5,6]
#types
example4 = np.array([1,2,3,4,5,6], dtype = "i4")

#resphaping
#array to matrix
example5 = np.array([1,2,3,4,5,6])
example5.repshate(2,3)
#array to tensor
example5 = np.array([1,2,3,4,5,6,7,8])
example5.respahe(2,2,2)

#matrix multiplication
example7 = np.array([[1, 2], [4, 5]])
example8 = np.array([[1, 2], [4, 5]])
outpt = np.matmul(example7, example8)