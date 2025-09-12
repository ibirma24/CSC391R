import numpy as np
import matplotlib.pyplot as plt

# Define global parameters
signal_freq = 5.0  # Signal frequency in Hz
duration = 2       # Duration in seconds
sampling_freq = 8  # Sampling frequency in Hz
num_bits = 3       # 3-bit quantization (8 levels: 0 - 7)
min_signal = -1    # Minimum signal value
max_signal = 1     # Maximum signal value

def original_signal(t):
    
    return np.sin(2 * np.pi * signal_freq * t)

# Create a figure for our plot
plt.figure(figsize=(12, 6))

# Step 1: Generate and plot the continuous signal
# Create 1000 evenly spaced time points
t_points = np.linspace(0, duration, 1000, endpoint=False)
# Calculate the continuous signal
cont_signal = original_signal(t_points)
# Plot the continuous signal
plt.plot(t_points, cont_signal, label='Continuous Signal')

# Step 2: Sample the signal
# Calculate number of samples needed
n = int(sampling_freq * duration)
# Create evenly spaced sampling points
t_sampled = np.linspace(0, duration, n, endpoint=False)
# Get signal values at sample points
sampled_signal = original_signal(t_sampled)
# Plot the sampled points
plt.plot(t_sampled, sampled_signal, 'ko', label='Sampled Points')

# Step 3: Quantize the sampled signal
# Calculate the number of quantization levels (2^num_bits)
num_levels = 2 ** num_bits

# First step of quantization: Scale and round to nearest integer level
qs = np.round((sampled_signal - min_signal) / (max_signal - min_signal) * (num_levels - 1))

# Second step: Convert back to signal values
qv = min_signal + qs * (max_signal - min_signal) / (num_levels - 1)

# Plot the quantized signal as a staircase
plt.step(t_sampled, qv, where='post', 
         label=f'Quantized Signal ({num_bits} bits)', 
         color='r', linestyle='--')

# Customize the plot
plt.title('Signal Sampling and Quantization Demonstration')
plt.xlabel('Time (seconds)')
plt.ylabel('Signal Amplitude')
plt.grid(True, alpha=0.3)
plt.legend()

# Add text box with parameters
param_text = f'Signal Frequency: {signal_freq} Hz\n'
param_text += f'Sampling Frequency: {sampling_freq} Hz\n'
param_text += f'Quantization: {num_bits} bits ({num_levels} levels)'
plt.text(0.02, 0.98, param_text, transform=plt.gca().transAxes,
         verticalalignment='top', bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))

plt.tight_layout()
plt.show()

# Print additional information
print("\nSignal Information:")
print("-" * 50)
print(f"Original signal: sin(2π * {signal_freq}t)")
print(f"Duration: {duration} seconds")
print(f"Number of samples: {n}")
print(f"Time between samples: {1/sampling_freq:.3f} seconds")
print(f"Quantization levels: {num_levels} (from {min_signal} to {max_signal})")
