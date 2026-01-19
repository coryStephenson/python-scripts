import numpy as np

# Hermitian (complex symmetric) matrix
A = np.array([[1, 2+3j, 4-5j],
              [2-3j, 5, 6+7j],
              [4+5j, 6-7j, 8]])

eigenvalues, eigenvectors = np.linalg.eigh(A)

print(f"\nEigenvalues:{eigenvalues}")
print(f"\nEigenvectors:\n{eigenvectors}")
