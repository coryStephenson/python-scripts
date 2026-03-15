import numpy as np
'''
The list b is a list of lists (rows and columns), so the 
NumPy array has 2 dimensions and array_b.ndim is 2.
'''

b = [[1, 2, 3], [4, 5, 6]]
array_b = np.array(b)
print(array_b.ndim)
