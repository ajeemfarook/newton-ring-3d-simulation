import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d import Axes3D  # For 3D plotting

# Parameters
wavelength = 589.3e-9  # Wavelength of light (in meters)
R = 0.5  # Radius of curvature of the lens (in meters)
n = 1.5  # Refractive index of the medium (glass)
d = 0.01  # Distance between the lens and the flat surface (in meters)
size = 0.001  # Size of the simulation area (in meters)
resolution = 75  # Resolution of the simulation (pixels per side)

# Create a grid of points
x = np.linspace(-size, size, resolution)
y = np.linspace(-size, size, resolution)
X, Y = np.meshgrid(x, y)
r = np.sqrt(X**2 + Y**2)  # Radial distance from the center

# Calculate the phase difference
phase_difference = (2 * np.pi / wavelength) * (2 * d + r**2 / (2 * R))

# Calculate the intensity
intensity = np.cos(phase_difference)**2

# Create the 3D figure and axis
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
ax.set_title("Newton's Rings Simulation (3D)")
ax.set_xlabel("X (mm)")
ax.set_ylabel("Y (mm)")
ax.set_zlabel("Intensity")

# Convert x and y to millimeters for better readability
X_mm = X * 1000
Y_mm = Y * 1000

# Plot the initial surface
surface = ax.plot_surface(X_mm, Y_mm, intensity, cmap='viridis', rstride=1, cstride=1, antialiased=True)

# Function to update the animation
def update(frame):
    global d
    d += 0.00001  # Increment the distance between the lens and the flat surface
    phase_difference = (2 * np.pi / wavelength) * (2 * d + r**2 / (2 * R))
    intensity = np.cos(phase_difference)**2
    ax.clear()  # Clear the previous frame
    ax.set_title(f"Newton's Rings Simulation (3D) - Frame {frame}")
    ax.set_xlabel("X (mm)")
    ax.set_ylabel("Y (mm)")
    ax.set_zlabel("Intensity")
    surface = ax.plot_surface(X_mm, Y_mm, intensity, cmap='grey', rstride=1, cstride=1, antialiased=True)
    return surface,

# Create the animation
ani = FuncAnimation(fig, update, frames=1, interval=2, blit=False)

# Show the animation
plt.show()
