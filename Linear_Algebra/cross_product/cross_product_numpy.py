import numpy as np

# Example vectors
A = np.array([1, 2, 3])
B = np.array([4, 5, 6])

# Compute cross product
cross_product = np.cross(A, B)
print(cross_product)  # Output: [-3, 6, -3] (1*(5-6) - 2*(4-6) + 3*(4-5))
