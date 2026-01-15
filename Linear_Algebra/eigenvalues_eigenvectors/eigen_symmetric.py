import numpy as np

# symmetric matrix or Hermitian for complex matrices 
A = np.array([[4, 1, 2],
              [1, 3, 1],
              [2, 1, 3]])
eigenvalues, eigenvectors = np.linalg.eig(A)

print("Matrix A:")
print(A)

print(f"\nEigenvalues: {eigenvalues:.3f}")
print(f"\nEigenvectors:\n{eigenvectors:.3f}")

