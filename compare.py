"""
The purpose of this file will be to compare images and delete duplicates on my PC in
order to free up immense space.


"""
import cv2
import numpy as np
from skimage.metrics import structural_similarity

# Load the image
image = cv2.imread("image1.jpg")

# Display image
cv2.imshow("Original",  image)
print(image.shape)
cv2.waitKey(0)
cv2.destroyAllWindows()

"""
# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Calculate the Laplacian of the image
lap = cv2.Laplacian(gray, cv2.CV_64F)

# Calculate the variance of the Laplacian
variance = np.var(lap)

# Calculate SSIM between the original and a sharpened version of the image
sharpened = cv2.filter2D(gray, -1, np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]]))
(score, diff) = compare_ssim(gray, sharpened, full=True)

# Print the results
print("Laplacian: {}".format(lap))
print("Variance of Laplacian: {}".format(variance))
print("SSIM: {}".format(score))

# Determine if the image is blurry
if variance < 100 or score < 0.9:
    print("Image is blurry")
else:
    print("Image is sharp")
"""
