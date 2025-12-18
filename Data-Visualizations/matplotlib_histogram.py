# Import statements
import matplotlib.pyplot as plt
import numpy as np

# Data
data = np.random.randn(1000)

# Plot
plt.hist(data,bins = 7, edgecolor='black', linewidth=1.2)
plt.show()



