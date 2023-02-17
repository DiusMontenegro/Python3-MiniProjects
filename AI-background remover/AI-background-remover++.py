import cv2
import numpy as np

# Load the input image
image = cv2.imread('input_image.png')

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply thresholding to create a mask
thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

# Find the contours of the objects in the image
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Create a blank mask to store the areas that will not be removed
mask = np.zeros(image.shape[:2], np.uint8)

# Iterate through the contours and remove the background
for cnt in contours:
    area = cv2.contourArea(cnt)
    if area < 5000:
        cv2.drawContours(mask, [cnt], -1, (255, 255, 255), -1)

# Apply the mask to the original image to remove the background
result = cv2.bitwise_and(image, image, mask=mask)

# Get user-specified background color
bg_color = input("Enter background color (e.g. white, black, blue, green, etc.): ")

# Convert background color to BGR format
colors = {'white': (255, 255, 255),
          'black': (0, 0, 0),
          'red': (0, 0, 255),
          'green': (0, 255, 0),
          'blue': (255, 0, 0),
          'yellow': (0, 255, 255),
          'magenta': (255, 0, 255),
          'cyan': (255, 255, 0)}

bg = colors.get(bg_color.lower(), (255, 255, 255))

# Create a new image with the specified background color
new_image = np.full_like(image, bg)

# Apply the mask to the new image to add transparency
new_image = cv2.bitwise_and(new_image, new_image, mask=cv2.bitwise_not(mask))

# Combine the original image with the new image
result = cv2.add(result, new_image)

# Save the result to a file
cv2.imwrite('output_image.png', result)
