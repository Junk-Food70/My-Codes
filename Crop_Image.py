import cv2
import matplotlib.pyplot as plt
image = cv2.imread('example.jpg')

# Convert BGR to RGB

# Cropping the image 
# Assume we know the region we want: rows 100 to 300, 200 to 400
cropped_image = image[100:300, 200:400]
cropped_rgb = cv2.cvtColor(cropped_image, cv2.COLOR_BGR2RGB)
plt.imshow(cropped_rgb)
plt.title("Cropped Region")
plt.show()