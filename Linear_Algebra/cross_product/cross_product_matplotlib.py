import warnings
warnings.filterwarnings("ignore")
import ipywidgets as widgets
import numpy as np
import matplotlib
matplotlib.use('TkAgg')  # Requires sudo apt install python3-tk; Try 'Qt5Agg' or 'QtAgg' if TkAgg doesn't work
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch
from mpl_toolkits.mplot3d import Axes3D, proj3d

class myArrow3D(FancyArrowPatch):
    def __init__(self, xs, ys, zs, arrowstyle="-|>", mutation_scale=50, **kwargs):
        super().__init__(
            (0, 0), (0, 0),  # Start and end points (will be overwritten)
            arrowstyle=arrowstyle,
            mutation_scale=mutation_scale,
            **kwargs
        )
        self._verts3d = xs, ys, zs  # Store 3D coordinates

    def do_3d_projection(self, renderer=None):
        xs3d, ys3d, zs3d = self._verts3d
        xs, ys, zs = proj3d.proj_transform(xs3d, ys3d, zs3d, self.axes.M)
        # Set arrow positions to the projected points
        self.set_positions((xs[0], ys[0]), (xs[1], ys[1]))
        return np.min(zs)

def vector3d(point, base=(0, 0, 0), ax=None, arrowstyle="-|>", mutation_scale=50, **kwargs):
    if ax is None:
        ax = plt.gca()
    # Create arrow from base to point
    arrow = myArrow3D(
        [base[0], point[0]],  # x-coordinates
        [base[1], point[1]],  # y-coordinates
        [base[2], point[2]],  # z-coordinates
        arrowstyle=arrowstyle,
        mutation_scale=mutation_scale,
        **kwargs
    )
    ax.add_patch(arrow)

def vector2d(point, base=(0, 0), ax=None, arrowstyle="-|>", mutation_scale=50, **kwargs):
    if ax is None:
        ax = plt.gca()
    arrow = FancyArrowPatch(
        base, point,
        arrowstyle=arrowstyle,
        mutation_scale=mutation_scale,
        **kwargs
    )
    ax.add_patch(arrow)

def plotVector(p, base=(0, 0), color=None, label=None, arrowstyle="-|>", mutation_scale=50, **kwargs):
    if len(p) == 2:
        vector2d(p, base=base, color=color, label=label, arrowstyle=arrowstyle, mutation_scale=mutation_scale, **kwargs)
    else:
        vector3d(p, base=base, color=color, label=label, arrowstyle=arrowstyle, mutation_scale=mutation_scale, **kwargs)

# Define vectors A and B
A = np.array([1, 2, 3])  # x-axis
B = np.array([4, 5, 6])  # y-axis

# Compute cross product
C = np.cross(A, B)
print("Cross product (C):", C)  # Output: [0, 0, 1]

# Plot in 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
plotVector(A, base=(0, 0, 0), color='r', label='A')
plotVector(B, base=(0, 0, 0), color='g', label='B')
plotVector(C, base=(0, 0, 0), color='b', label='A × B', arrowstyle="-|>")
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_xlim((0, 6))
ax.set_ylim((0, 6))
ax.set_zlim((0, 6))
ax.legend()
plt.title("Cross Product Visualization")
plt.show()
