import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def compute_norm_and_plot(vector):
    # Convert to numpy array for easier handling
    v = np.array(vector)

    # Compute norm
    norm = np.linalg.norm(v)

    # Plot components
    fig = plt.figure(figsize=(8, 6))

    # --- 2D Plot ---
    if len(v) == 2:
        plt.subplot(1, 2, 1)
        plt.arrow(0, 0, v[0], v[1], color='blue', head_width=0.1, head_length=0.1)
        plt.plot(v[0], v[1], 'ro')  # Endpoint
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.title(f'Vector: ({v[0]}, {v[1]})\nNorm = {norm:.2f}')

        # Plot components as arrows
        plt.arrow(0, 0, v[0], 0, color='green', alpha=0.5, label='X-component')
        plt.arrow(0, 0, 0, v[1], color='red', alpha=0.5, label='Y-component')
        plt.legend()

    # --- 3D Plot ---
    elif len(v) == 3:
        ax = fig.add_subplot(1, 2, 2, projection='3d')
        ax.quiver(0, 0, 0, v[0], v[1], v[2], color='blue', length=1.5, arrow_length_ratio=0.1)
        ax.plot(v[0], v[1], v[2], 'ro')  # Endpoint
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        ax.set_title(f'Vector: ({v[0]}, {v[1]}, {v[2]})\nNorm = {norm:.2f}')

        # Plot components as arrows
        ax.quiver(0, 0, 0, v[0], 0, 0, color='green', length=1.5, arrow_length_ratio=0.1)
        ax.quiver(0, 0, 0, 0, v[1], 0, color='red', length=1.5, arrow_length_ratio=0.1)
        ax.quiver(0, 0, 0, 0, 0, v[2], color='purple', length=1.5, arrow_length_ratio=0.1)

    else:
        raise ValueError("Vector must be 2D or 3D.")

    plt.tight_layout()
    plt.show()

# Example usage:
vector_2d = (3, 4)  # Replace with your vector
vector_3d = (1, -2, np.sqrt(5))  # Replace with your vector

compute_norm_and_plot(vector_2d)  # For 2D
compute_norm_and_plot(vector_3d)  # For 3D
