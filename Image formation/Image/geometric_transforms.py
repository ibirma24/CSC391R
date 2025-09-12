import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read the original image
og_image = cv2.imread('Image formation/Image/original_image.jpg')
if og_image is None:
    print("Error: Could not load original_image.jpg")
    exit()

# Read the transformed image we need to match
tf_image = cv2.imread('Image formation/Image/transformed_image.jpg')
if tf_image is None:
    print("Error: Could not load transformed_image.jpg")
    exit()


# First, let's try moving the image to the right by 50 pixels and down by 30 pixels
t_matrix = np.float32([[1, 0, 50], [0, 1, 30]])
t_image = cv2.warpAffine(og_image, t_matrix, (og_image.shape[1], og_image.shape[0]))

# Now, let's rotate the translated image by 45 degrees
# Get the image center point
center = (og_image.shape[1] // 2, og_image.shape[0] // 2)
r_matrix = cv2.getRotationMatrix2D(center, 45, 1.0)
rotated_image = cv2.warpAffine(t_image, r_matrix, (og_image.shape[1], og_image.shape[0]))

# Finally, let's scale the image to make it a bit smaller
scale_factor = 0.8
scale_matrix = np.float32([[scale_factor, 0, 0], [0, scale_factor, 0]])
final_image = cv2.warpAffine(rotated_image, scale_matrix, (og_image.shape[1], og_image.shape[0]))

og_rgb = cv2.cvtColor(og_image, cv2.COLOR_BGR2RGB)
tf_rgb = cv2.cvtColor(tf_image, cv2.COLOR_BGR2RGB)
final_rgb = cv2.cvtColor(final_image, cv2.COLOR_BGR2RGB)


plt.figure(figsize=(15, 5))

# Show original image
plt.subplot(131)
plt.imshow(og_rgb)
plt.title('Original Image')
plt.axis('off')

# Show target transformed image
plt.subplot(132)
plt.imshow(tf_rgb)
plt.title('Transformed Image')
plt.axis('off')

# Show our attempt at matching the transformation
plt.subplot(133)
plt.imshow(final_rgb)
plt.title('Reverse Engineered Image')
plt.axis('off')

# Print the transformations we applied
print("Transformations applied:")
print("1. Translation: moved right by 50 pixels and down by 30 pixels")
print("2. Rotation: rotated by 45 degrees around the center")
print("3. Scaling: scaled down to 80% of original size")

# Save our result
cv2.imwrite('reverse_engineered.jpg', final_image)

# Show all the images
plt.show()
