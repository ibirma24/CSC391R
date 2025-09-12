import numpy as np
import matplotlib.pyplot as plt

# Define global parameters
signal_freq = 5.0  # Signal frequency in Hz
duration = 2       # Duration in seconds
sampling_freq = 8  # Sampling frequency in Hz
num_bits = 3       # 3-bit quantization (8 levels: 0 - 7)
min_signal = -1    # Minimum signal value
max_signal = 1     # Maximum signal value

# Noise parameters
mean = 0          # Mean of Gaussian noise
std_dev = 0.1     # Standard deviation of noise (noise level)

def original_signal(t):
    """Generate the original continuous signal: sin(2πft)"""
    return np.sin(2 * np.pi * signal_freq * t)

def add_gaussian_noise(signal, mean, std):
    
    mag = np.max(signal) - np.min(signal)  # Signal magnitude
    noise = np.random.normal(mean, std * mag, len(signal))
    return signal + noise

def quantize_signal(signal, num_bits, min_val, max_val):
   
    num_levels = 2 ** num_bits
    # Scale and round to nearest integer level
    qs = np.round((signal - min_val) / (max_val - min_val) * (num_levels - 1))
    # Convert back to signal values
    return min_val + qs * (max_val - min_val) / (num_levels - 1)

def calculate_error_metrics(original, noisy):
    """
    Calculate MSE, RMSE, and PSNR between original and noisy signals
    """
    # Mean Square Error
    mse = np.mean((original - noisy) ** 2)
    
    # Root Mean Square Error
    rmse = np.sqrt(mse)
    
    # Peak Signal to Noise Ratio
    max_signal = np.max(np.abs(original))
    psnr = 10 * np.log10(max_signal ** 2 / mse)
    
    return mse, rmse, psnr

# Create time points
t_points = np.linspace(0, duration, 1000, endpoint=False)  # Original signal points
n = int(sampling_freq * duration)  # Number of samples
t_sampled = np.linspace(0, duration, n, endpoint=False)    # Sampling points

# Generate signals
original_cont = original_signal(t_points)
sampled_signal = original_signal(t_sampled)

# Add noise to sampled signal
noisy_signal = add_gaussian_noise(sampled_signal, mean, std_dev)

# Quantize both clean and noisy signals
quantized_clean = quantize_signal(sampled_signal, num_bits, min_signal, max_signal)
quantized_noisy = quantize_signal(noisy_signal, num_bits, min_signal, max_signal)

# Calculate error metrics
mse, rmse, psnr = calculate_error_metrics(quantized_clean, quantized_noisy)

# Create the plot
plt.figure(figsize=(12, 8))

# Plot original continuous signal
plt.plot(t_points, original_cont, 'b-', label='Original Signal', alpha=0.5)

# Plot sampled and quantized signal (clean)
plt.step(t_sampled, quantized_clean, 'g--', where='post', 
         label='Clean Quantized Signal', alpha=0.5)

# Plot sampled and quantized signal (noisy)
plt.step(t_sampled, quantized_noisy, 'r--', where='post',
         label=f'Noisy Quantized Signal (σ={std_dev})')

# Plot the noisy samples
plt.plot(t_sampled, noisy_signal, 'ko', label='Noisy Samples', 
         markersize=4, alpha=0.5)

# Customize the plot
plt.title('Signal Sampling and Quantization with Gaussian Noise')
plt.xlabel('Time (seconds)')
plt.ylabel('Signal Amplitude')
plt.grid(True, alpha=0.3)
plt.legend()

# Add text box with parameters and error metrics
info_text = f'Signal Freq: {signal_freq} Hz\n'
info_text += f'Sampling Freq: {sampling_freq} Hz\n'
info_text += f'Quantization: {num_bits} bits\n'
info_text += f'Noise σ: {std_dev}\n'
info_text += f'MSE: {mse:.6f}\n'
info_text += f'RMSE: {rmse:.6f}\n'
info_text += f'PSNR: {psnr:.2f} dB'

plt.text(0.02, 0.98, info_text, transform=plt.gca().transAxes,
         verticalalignment='top', bbox=dict(boxstyle='round', 
         facecolor='white', alpha=0.8))

plt.tight_layout()
plt.show()

# Print detailed error metrics
print("\nError Metrics:")
print("-" * 50)
print(f"Mean Square Error (MSE): {mse:.6f}")
print(f"Root Mean Square Error (RMSE): {rmse:.6f}")
print(f"Peak Signal-to-Noise Ratio (PSNR): {psnr:.2f} dB")
