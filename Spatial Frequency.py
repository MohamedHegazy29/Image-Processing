import cv2
import numpy as np
import matplotlib.pyplot as plt

mask3High_1 = np.array([
    [0, -1, 0],
    [-1, 5, -1],
    [0, -1, 0]], dtype=np.float32)

mask3High_2 = np.array([
    [-1, -1, -1],
    [-1, 9, -1],
    [-1, -1, -1]], dtype=np.float32)

mask3High_3 = np.array([
    [1, -2, 1],
    [-2, 5, -2],
    [1, -2, 1]], dtype=np.float32)

mask3Low_1 = np.array([
    [0, 1 / 6, 0],
    [1 / 6, 2 / 6, 1 / 6],
    [0, 1 / 6, 0]], dtype=np.float32)

mask3Low_2 = np.array([
    [1/9, 1/9, 1/9],
    [1/9, 1/9, 1/9],
    [1/9, 1/9, 1/9]], dtype=np.float32)

mask3Low_3 = np.array([
    [1/16, 2/16, 1/16],
    [2 / 16, 4 / 16, 2 / 16],
    [1/16, 2 / 16, 1/16]], dtype=np.float32)

mask3Low_4 = np.array([
    [1/10,1/10, 1/10],
    [1/10, 2/10, 1/10],
    [1/10,1/10, 1/10]], dtype=np.float32)

def conv(image, mask1):

    result = cv2.filter2D(image, -1, mask1)
    return result

def median_filter(image):
   
    height, width = image.shape
    filtered_image = np.zeros_like(image)

    for i in range(1, height - 1):
        for j in range(1, width - 1):
            neighborhood = image[i - 1:i + 2, j - 1:j + 2]
            median_value = np.median(neighborhood)
            filtered_image[i, j] = median_value

    return filtered_image

# Load the image
img = cv2.imread('/Applications/Python 3.7/ImgProject/images/house.png', cv2.IMREAD_GRAYSCALE)

# Apply filters
lowpass = conv(img, mask3Low)
highpass = conv(img, mask3High)
median = median_filter(img)

# Display results using matplotlib
plt.figure(figsize=(20, 10))

plt.subplot(2, 2, 1)
plt.title('Original')
plt.imshow(img, cmap='gray')
plt.axis('off')

plt.subplot(2, 2, 2)
plt.title('Low-pass Filtered')
plt.imshow(lowpass, cmap='gray')
plt.axis('off')

plt.subplot(2, 2, 3)
plt.title('High-pass Filtered')
plt.imshow(highpass, cmap='gray')
plt.axis('off')

plt.subplot(2, 2, 4)
plt.title('Median Filtered')
plt.imshow(median, cmap='gray')
plt.axis('off')

plt.show()
