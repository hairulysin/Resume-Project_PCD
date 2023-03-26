import cv2
import numpy as np

# Load the image in RGB format
img = cv2.imread('lena.jpg', cv2.IMREAD_COLOR)

# Convert RGB image to CMY
cmy_img = 1 - (img / 255.0)

# Display the CMY image
cv2.imshow('CMY Image', cmy_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
