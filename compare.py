"""
The purpose of this file will be to compare images and delete duplicates on my PC in
order to free up immense space.


I will be using openCV to complete this.

"""


# Importing the module
import cv2
# import skimage

# Choose image
original = cv2.imread("02.JPG")

# Display image
cv2.imshow("Original",  original)
print(original.shape)
cv2.waitKey(0)
cv2.destroyAllWindows()
