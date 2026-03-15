import numpy as np
'''
The array has 2 nested lists (rows) and each nested list 
has 4 elements (columns), so the shape attribute 
returns the tuple (2, 4).
'''

b = np.array([[2, 4, 6, 8], [1, 3, 5, 7]])
print(b.shape)
