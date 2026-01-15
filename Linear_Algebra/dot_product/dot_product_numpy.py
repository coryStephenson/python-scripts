import numpy as np

# Example vectors
A = np.array([1, 2, 3])
B = np.array([4, 5, 6])

# Compute dot product
dot_product = np.dot(A, B)  # or A @ B (element-wise multiplication + sum)
print(dot_product)  # Output: 32 (1*4 + 2*5 + 3*6)
