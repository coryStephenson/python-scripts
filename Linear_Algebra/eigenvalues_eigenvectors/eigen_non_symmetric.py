import numpy as np
from scipy.linalg import eig

# non-symmetric matrix
A = np.array([[2, -1, 0],
              [0, 2, -1],
              [1, 0, 2]])

print(f"Matrix A:")
print(A)

eigenvalues, eigenvectors = eig(A)

print(f"\nEigenvalues: {eigenvalues:.3f}")
print(f"\nEigenvectors:\n{eigenvectors:.3f}")
