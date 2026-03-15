import numpy as np
'''
In 2D NumPy slicing, the first index selects the first row 
and the second slice 0:2 selects the first two columns of 
that row, giving [2 4].
'''

b = np.array([[2, 4, 6],
              [8, 10, 12]])

print(b[0, 0:2])
