# CSC391R - Image Formation and Processing Projects


1. Signal Sampling and Quantization
Explores how continuous signals are converted into digital form through sampling and quantization processes.

Signal sampling at different frequencies
Sample output shows a sine wave being sampled and quantized
Need at least 10 Hz sampling frequency (2 × signal frequency) to avoid aliasing
3-bit quantization provides rough approximation; more bits give smoother results
Trade-off between data size and signal quality

2. Error and Noise Analysis
Investigates the effects of noise on signals and various error metrics.

Features:
Gaussian noise generation and addition
Error measurements (MSE, RMSE, PSNR)
Visual comparison of original vs. noisy signals

Key metrics calculated:
Mean Square Error (MSE): Measures average squared difference
Root Mean Square Error (RMSE): Square root of MSE, more intuitive
Peak Signal-to-Noise Ratio (PSNR): Signal strength vs. noise in dB

3. Lens and Aperture Parameters
Studies the relationships between various camera lens parameters.


Thin Lens Formula Analysis:
Maps object distance to image distance
   Shows behavior for different focal lengths (3mm, 9mm, 50mm, 200mm)
Demonstrates near vs. far focus characteristics

 Aperture Analysis:
 Compares different lens types (prime vs. zoom)
Shows relationship between focal length and aperture diameter
Demonstrates f-number effects


 4. Geometric Transformations
Demonstrates basic image transformations using OpenCV.

Transformations implemented:
Translation: Moving image by (50, 30) pixels
Rotation: 45-degree rotation around center
Scaling: 80% size reduction

Results show:
- Original image
- Target transformed image
- Reverse engineered transformation









