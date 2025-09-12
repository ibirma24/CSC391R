# Import the libraries we need
import numpy as np  # For math operations
import matplotlib.pyplot as plt  # For making plots

def thin_lens_zi(f, z0): #Thin lens formula to calculate image distance
    zi = (f * z0) / (z0 - f)
    return zi

# Make a new figure for our first plot
plt.figure(figsize=(10, 6))

# Define our focal lengths (in millimeters)
focal_lengths = [3, 9, 50, 200]

# Create the range of object distances
smallest_f = min(focal_lengths)  # Find smallest focal length
z0_start = 1.1 * smallest_f  # Start a bit after the smallest focal length
z0_end = 10000  # End at 10^4 mm
points_per_mm = 4  # We want 4 points per millimeter
total_points = int((z0_end - z0_start) * points_per_mm)

# Create array of z0 values using logarithmic spacing
z0 = np.logspace(np.log10(z0_start), np.log10(z0_end), total_points)

# Make a list of colors for our plots
colors = ['blue', 'green', 'red', 'purple']

# Plot for each focal length
for i in range(len(focal_lengths)):
    f = focal_lengths[i]  # Get the focal length
    color = colors[i]  # Get the color
    
    # Calculate image distance for this focal length
    zi = thin_lens_zi(f, z0)
    
    # Plot the curve using loglog scale
    plt.loglog(z0, zi, color=color, label=f'f = {f}mm')
    
    # Add vertical line at z0 = f
    plt.axvline(x=f, color=color, linestyle='--', alpha=0.5)

# Make the plot look nice
plt.title('Lens-to-Image Distance vs Object Distance')
plt.xlabel('Object Distance (mm)')
plt.ylabel('Image Distance (mm)')
plt.ylim(0, 3000)  # Set y-axis limits
plt.grid(True, which='both', alpha=0.2)  # Add grid lines
plt.legend()  # Add legend

# Show the first plot
plt.show()


# Make a new figure for our second plot
plt.figure(figsize=(12, 8))

# Define our list of lenses
lenses = [
    {"name": "24mm Wide Angle", "focal_length": 24, "f_number": 1.4},
    {"name": "50mm Standard", "focal_length": 50, "f_number": 1.8},
    {"name": "70-200mm Zoom", "focal_length": [70, 200], "f_number": 2.8},
    {"name": "400mm Telephoto", "focal_length": 400, "f_number": 2.8},
    {"name": "600mm Super Telephoto", "focal_length": 600, "f_number": 4.0}
]

# First, let's calculate and print the aperture diameters
print("\nAperture Diameter Calculations:")
print("-" * 40)

for lens in lenses:
    if isinstance(lens["focal_length"], list):
        # This is a zoom lens with a range of focal lengths
        min_f = lens["focal_length"][0]
        max_f = lens["focal_length"][1]
        
        # Calculate diameter at both ends of zoom range
        min_d = min_f / lens["f_number"]
        max_d = max_f / lens["f_number"]
        
        print(f"\n{lens['name']}:")
        print(f"  At {min_f}mm: {min_d:.1f}mm aperture")
        print(f"  At {max_f}mm: {max_d:.1f}mm aperture")
    else:
        # This is a prime lens (single focal length)
        d = lens["focal_length"] / lens["f_number"]
        print(f"\n{lens['name']}:")
        print(f"  Aperture diameter: {d:.1f}mm")

# Now let's make the plot
# Create range of focal lengths for the lines
f = np.linspace(0, 600, 1000)

# Plot lines for different f-numbers
f_numbers = [1.4, 1.8, 2.8, 4.0]
colors = ['blue', 'green', 'red', 'purple']

# Plot a line for each f-number
for f_num, color in zip(f_numbers, colors):
    diameter = f / f_num  # Calculate diameter
    plt.plot(f, diameter, color=color, label=f'f/{f_num}')

# Plot actual lenses as points
markers = ['o', 's', '^', 'D', '*']  # Different marker for each lens
for lens, marker in zip(lenses, markers):
    if isinstance(lens["focal_length"], list):
        # Plot zoom lens (both ends connected by line)
        f_values = lens["focal_length"]
        diameters = [f / lens["f_number"] for f in f_values]
        plt.plot(f_values, diameters, 'k--', marker=marker, 
                 label=f"{lens['name']} (f/{lens['f_number']})")
    else:
        # Plot prime lens (single point)
        d = lens["focal_length"] / lens["f_number"]
        plt.plot(lens["focal_length"], d, 'black', marker=marker, 
                 markersize=10, label=f"{lens['name']} (f/{lens['f_number']})")

# Make the plot look nice
plt.title('Aperture Diameter vs Focal Length')
plt.xlabel('Focal Length (mm)')
plt.ylabel('Aperture Diameter (mm)')
plt.grid(True, alpha=0.2)
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()

# Show the second plot
plt.show()
