import numpy as np
'''
Passing the nested list to np.array creates a 2D NumPy 
array where each inner list is a row, and printing it 
shows the rectangular layout as [[1 2 3] [4 5 6]] on two 
lines.
'''

b = [[1, 2, 3], [4, 5, 6]]
array_b = np.array(b)
print(array_b)
