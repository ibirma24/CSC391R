
import numpy as np
import matplotlib.pyplot as plt

signal_freq = 5.0  # This is how many times our signal goes up and down per second (in Hz)
duration = 2       # This is how long we want to look at our signal (in seconds)
sampling_freq = 8  # This is how many times per second we measure our signal (in Hz)
num_bits = 3       # This tells us how precise our measurements are (3 bits means 8 different levels)
min_signal = -1    # The lowest value our signal can have
max_signal = 1     # The highest value our signal can have

# This function creates our original sine wave signal
def original_signal(t):
    # The formula for a sine wave is: sin(2π * frequency * time)
    # 2π is about 6.28, we multiply this by our frequency and time
    # This gives us a wave that goes up and down smoothly between -1 and 1
    return np.sin(2 * np.pi * signal_freq * t)

# Create a figure for our plot
plt.figure(figsize=(12, 6))

# Create 1000 evenly spaced time points
t_points = np.linspace(0, duration, 1000, endpoint=False)
# Calculate the continuous signal
cont_signal = original_signal(t_points)
# Plot the continuous signal
plt.plot(t_points, cont_signal, label='Continuous Signal')

# Calculate number of samples needed
n = int(sampling_freq * duration)
# Create evenly spaced sampling points
t_sampled = np.linspace(0, duration, n, endpoint=False)
# Get signal values at sample points
sampled_signal = original_signal(t_sampled)
# Plot the sampled points
plt.plot(t_sampled, sampled_signal, 'ko', label='Sampled Points')

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

# Print helpful information about our signal
print("\nSignal Information:")
print("-" * 50)
print(f"Original signal: sin(2π * {signal_freq}t)")
print(f"Duration: {duration} seconds")
print(f"Number of samples: {n}")
print(f"Time between samples: {1/sampling_freq:.3f} seconds")
print(f"Quantization levels: {num_levels} (from {min_signal} to {max_signal})")

# Let's talk about the Nyquist frequency
# The Nyquist-Shannon sampling theorem says we need to sample at least twice as fast as our signal frequency
nyquist_freq = 2 * signal_freq
print("\nImportant Note about Sampling Frequency:")
print("-" * 50)
print(f"To capture the true shape of our signal, we need to sample at least {nyquist_freq} times per second")
print(f"Our current sampling frequency is {sampling_freq} Hz")

if sampling_freq >= nyquist_freq:
    print("Good news! Our sampling frequency is fast enough to capture the signal correctly!")
else:
    print("Warning: Our sampling frequency is too low!")
    print("This might make our signal look different than it really is (this is called aliasing)")

print("\nHow to Make Our Digital Signal Better:")
print("-" * 50)
print("1. Take more samples (increase sampling_freq)")
print("   - This helps us catch more details of how the signal changes")
print("2. Use more bits (increase num_bits)")
print("   - This gives us more precise measurements")
print("   - Current precision: {} different levels".format(2**num_bits))
