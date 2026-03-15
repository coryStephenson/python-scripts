import numpy as np
'''
NumPy uses element-wise (Hadamard) multiplication 
with *, so each position is multiplied separately, 
giving [[ 2 0] [15 4]].
'''

X = np.array([[1, 2], [3, 4]])
Y = np.array([[2, 0], [5, 1]])
Z = X * Y
print(Z)
