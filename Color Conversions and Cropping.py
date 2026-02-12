import cv2
import matplotlib.pyplot as plt
image = cv2.imread("CuteCat.jpg")

# Check if image loaded successfully
if image is None:
    print("Error: Could not load image. Check file path.")
    exit()

# Convert BGR to RGB

image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
plt.imshow(image_rgb)
plt.title("RGB Image")
plt.axis('off')
plt.show()

# Convert to Grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
plt.imshow(gray_image, cmap='gray')
plt.title("Grayscale Image")
plt.axis('off')
plt.show()

# Cropping the image 
# Assume we know the region we want: rows 100 to 300, 200 to 400
cropped_image = image[100:300, 200:400]
cropped_rgb = cv2.cvtColor(cropped_image, cv2.COLOR_BGR2RGB)
plt.imshow(cropped_rgb)
plt.title("Cropped Region")
plt.axis('off')
plt.show()
