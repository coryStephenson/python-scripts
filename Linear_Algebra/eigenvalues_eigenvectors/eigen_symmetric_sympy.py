from sympy import Matrix

A = Matrix([[4, 1, 2], [1, 3, 1], [2, 1, 3]])

# Compute eigenvalues
eigenvalues = A.eigenvals()

# Compute eigenvectors
eigenvectors = A.eigenvects()

# Eigenvalues
print("Eigenvalues:", eigenvalues)

# Eigenvectors (returns a list of eigenvector tuples)
print("Eigenvectors:", eigenvectors)
