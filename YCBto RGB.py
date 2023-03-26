import cv2
import numpy as np

# Load the image in RGB format
img = cv2.imread('lena.jpg', cv2.IMREAD_COLOR)

# Convert RGB image to HSL
hsl_img = cv2.cvtColor(img, cv2.COLOR_BGR2HLS)

# Display the HSL image
cv2.imshow('HSL Image', hsl_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
