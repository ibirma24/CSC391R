import numpy as np
import matplotlib.pyplot as plt

signal_freq = 5.0  # How many times the signal goes up and down per second
duration = 2       # How long we want to look at the signal
sampling_freq = 8  # How many times per second we measure the signal
num_bits = 3       # How precise our measurements are (3 bits = 8 levels)
min_signal = -1    # Lowest value our signal can have
max_signal = 1     # Highest value our signal can have

mean = 0          # Center of our noise distribution
std_dev = 0.1     # How spread out our noise is (noise level)

# This function creates our original sine wave signal (same as before)
def original_signal(t):
    return np.sin(2 * np.pi * signal_freq * t)

# This is our new function that adds noise to a signal
def add_gaussian_noise(signal, mean, std):
    # First, find out how big our signal is
    mag = np.max(signal) - np.min(signal)
    
    # Create random noise with the same length as our signal
    # np.random.normal creates random numbers that follow a bell curve pattern
    noise = np.random.normal(mean, std * mag, len(signal))
    
    # Add the noise to our signal
    noisy_signal = signal + noise
    
    return noisy_signal

# Create time points for our continuous signal
t_points = np.linspace(0, duration, 1000, endpoint=False)
cont_signal = original_signal(t_points)

# Add noise to our continuous signal
noisy_cont_signal = add_gaussian_noise(cont_signal, mean, std_dev)

# Sample the signal (take measurements at specific times)
n = int(sampling_freq * duration)
t_sampled = np.linspace(0, duration, n, endpoint=False)
sampled_signal = original_signal(t_sampled)
noisy_sampled = add_gaussian_noise(sampled_signal, mean, std_dev)

# Quantize the noisy sampled signal (convert to digital levels)
num_levels = 2 ** num_bits
# Scale and round to nearest level
qs = np.round((noisy_sampled - min_signal) / (max_signal - min_signal) * (num_levels - 1))
# Convert back to signal values
quantized_values = min_signal + qs * (max_signal - min_signal) / (num_levels - 1)

# Create a new figure for our plot
plt.figure(figsize=(12, 6))

# Plot all our signals
plt.plot(t_points, cont_signal, 'b-', label='Original Signal', alpha=0.5)
plt.plot(t_points, noisy_cont_signal, 'g-', label='Noisy Signal', alpha=0.3)
plt.plot(t_sampled, noisy_sampled, 'go', label='Noisy Samples')
plt.step(t_sampled, quantized_values, 'r--', where='post', 
         label=f'Quantized Signal ({num_bits} bits)')

# Make the plot look nice
plt.title('Signal with Noise, Sampling, and Quantization')
plt.xlabel('Time (seconds)')
plt.ylabel('Signal Value')
plt.grid(True, alpha=0.3)
plt.legend()

# Show the plot
plt.show()

# Now let's calculate the errors

# 1. Mean Square Error (MSE)
# This tells us how different our noisy signal is from the original
mse = np.mean((sampled_signal - noisy_sampled) ** 2)

# 2. Root Mean Square Error (RMSE)
# This is just the square root of MSE
rmse = np.sqrt(mse)

# 3. Peak Signal-to-Noise Ratio (PSNR)
# This tells us how strong our signal is compared to the noise
max_signal_value = np.max(np.abs(sampled_signal))
psnr = 10 * np.log10(max_signal_value ** 2 / mse)

# Print our results
print("\nError Measurements:")
print("-" * 50)
print(f"Mean Square Error (MSE): {mse:.6f}")
print(f"Root Mean Square Error (RMSE): {rmse:.6f}")
print(f"Peak Signal-to-Noise Ratio (PSNR): {psnr:.2f} dB")

print("\nWhat do these numbers mean?")
print("-" * 50)
print("MSE: How different our noisy signal is from the original")
print("     - Smaller numbers mean less noise")
print("RMSE: Similar to MSE but easier to understand")
print("      - It's in the same units as our signal")
print("PSNR: How strong our signal is compared to the noise")
print("      - Bigger numbers (more dB) mean better signal quality")
print(f"      - Above 30 dB is usually good, we got {psnr:.2f} dB")
