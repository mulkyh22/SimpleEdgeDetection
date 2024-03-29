# -*- coding: utf-8 -*-
"""EdgeDetection.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/111MORERHpE6oPnVV9V4uqiNrTovI9e3f
"""

from google.colab.patches import cv2_imshow
import cv2
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import time

# Input Image
# Insert 'Image.jpg' to the files
img = cv2.imread('image.jpg')
print ("Original")
cv2_imshow(img)

#Image2Grayscale
start_time = cv2.getTickCount()
img_blur = cv.GaussianBlur(img_gray,(3,3),0)
end_time = cv2.getTickCount()
time_in_ms = (end_time - start_time) * 1000 / cv2.getTickFrequency()

#Output
print ("Original")
cv2_imshow(img)
print ("Grayscale")
cv2_imshow(img_blur)


print("--------------------------------------------------")
print(f"Grayscale took {time_in_ms:.2f} ms")

# Thresholding
# Apply thresholding to the grayscale image
start_time1 = cv2.getTickCount()
ret, thresh1 = cv2.threshold(img_blur, 90, 255, cv2.THRESH_BINARY)
end_time1 = cv2.getTickCount()
time_in_ms1 = (end_time1 - start_time1) * 1000 / cv2.getTickFrequency()

start_time2 = cv2.getTickCount()
ret, thresh2 = cv2.threshold(img_blur, 127, 255, cv2.THRESH_BINARY_INV)
end_time2 = cv2.getTickCount()
time_in_ms2 = (end_time2 - start_time2) * 1000 / cv2.getTickFrequency()

start_time3 = cv2.getTickCount()
ret, thresh3 = cv2.threshold(img_blur, 127, 255, cv2.THRESH_TRUNC)
end_time3 = cv2.getTickCount()
time_in_ms3 = (end_time3 - start_time3) * 1000 / cv2.getTickFrequency()

start_time4 = cv2.getTickCount()
ret, thresh4 = cv2.threshold(img_blur, 127, 255, cv2.THRESH_TOZERO)
end_time4 = cv2.getTickCount()
time_in_ms4 = (end_time4 - start_time4) * 1000 / cv2.getTickFrequency()

start_time5 = cv2.getTickCount()
ret, thresh5 = cv2.threshold(img_blur, 127, 255, cv2.THRESH_TOZERO_INV)
end_time5 = cv2.getTickCount()
time_in_ms5 = (end_time5 - start_time5) * 1000 / cv2.getTickFrequency()

# Display the original grayscale image and the thresholded images
print("Result")
print("--------------------------------------------------")
print ("Original")
cv2_imshow(img)
print ("Grayscale")
cv2_imshow(img_blur)
print("--------------------------------------------------")
print ("Thresholding 1")
cv2_imshow(thresh1)
print ("Thresholding 2")
cv2_imshow(thresh2)
print ("Thresholding 3")
cv2_imshow(thresh3)
print ("Thresholding 4")
cv2_imshow(thresh4)
print ("Thresholding 5")
cv2_imshow(thresh5)
print("--------------------------------------------------")
print("Performance Stats")
print(f"Thresholding 1 detection took {time_in_ms1:.2f} ms")
print(f"Thresholding 2 detection took {time_in_ms2:.2f} ms")
print(f"Thresholding 3 detection took {time_in_ms3:.2f} ms")
print(f"Thresholding 4 detection took {time_in_ms4:.2f} ms")
print(f"Thresholding 5 detection took {time_in_ms5:.2f} ms")

# Sobel Edge Detection
start_time1 = cv2.getTickCount()
sobelx = cv2.Sobel(img_blur, cv2.CV_64F, 1, 0, ksize=3)
end_time1 = cv2.getTickCount()
time_in_ms1 = (end_time1 - start_time1) * 1000 / cv2.getTickFrequency()

start_time2 = cv2.getTickCount()
sobely = cv2.Sobel(img_blur, cv2.CV_64F, 0, 1, ksize=3)
end_time2 = cv2.getTickCount()
time_in_ms2 = (end_time2 - start_time2) * 1000 / cv2.getTickFrequency()

start_time3 = cv2.getTickCount()
sobelxy = cv2.Sobel(img_blur, cv2.CV_64F, 1, 1, ksize=3)
end_time3 = cv2.getTickCount()
time_in_ms3 = (end_time3 - start_time3) * 1000 / cv2.getTickFrequency()

#Output
print("Result")
print("--------------------------------------------------")
print ("Original")
cv2_imshow(img)
print ("Grayscale")
cv2_imshow(img_blur)
print("--------------------------------------------------")
print ("Sobel x")
cv2_imshow(sobelx)
print ("Sobel y")
cv2_imshow(sobely)
print ("Sobel xy")
cv2_imshow(sobelxy)

print("--------------------------------------------------")
print("Performance Stats")
print(f"Sobel edge x detection took {time_in_ms1:.2f} ms")
print(f"Sobel edge y detection took {time_in_ms2:.2f} ms")
print(f"Sobel edge z detection took {time_in_ms3:.2f} ms")

# Compare Original - Canny Edge

start_time = cv2.getTickCount()
edges = cv2.Canny(img_blur, 100, 200)
end_time = cv2.getTickCount()
time_in_ms = (end_time - start_time) * 1000 / cv2.getTickFrequency()

# Display the original image and the Canny edge detection result
print("Result")
print("--------------------------------------------------")
print ("Original")
cv2_imshow(img)
print ("Grayscale")
cv2_imshow(img_blur)
print("--------------------------------------------------")
print("Canny")
cv2_imshow(edges)

print("--------------------------------------------------")
print("Performance Stats")
print(f"Canny edge detection took {time_in_ms:.2f} ms")

# Prewitt Edge Detection


# Apply Prewitt edge detection
start_time1 = cv2.getTickCount()
kernelx = np.array([[1, 0, -1], [1, 0, -1], [1, 0, -1]])
prewittx = cv2.filter2D(img_blur, -1, kernelx)
end_time1 = cv2.getTickCount()
time_in_ms1 = (end_time1 - start_time1) * 1000 / cv2.getTickFrequency()

start_time2 = cv2.getTickCount()
kernely = np.array([[-1, -1, -1], [0, 0, 0], [1, 1, 1]])
prewitty = cv2.filter2D(img_blur, -1, kernely)
end_time2 = cv2.getTickCount()
time_in_ms2 = (end_time2 - start_time2) * 1000 / cv2.getTickFrequency()

# Display the original image and the Prewitt X and Y results
print("Result")
print("--------------------------------------------------")
print ("Original")
cv2_imshow(img)
print ("Grayscale")
cv2_imshow(img_blur)
print("--------------------------------------------------")
print ("Prewitt X")
cv2_imshow(prewittx)
print ("Prewitt Y")
cv2_imshow(prewitty)


print("--------------------------------------------------")
print("Performance Stats")
print(f"Prewitt X edge detection took {time_in_ms1:.2f} ms")
print(f"Prewitt Y edge detection took {time_in_ms2:.2f} ms")

# Laplace Edge Detection
start_time = cv2.getTickCount()
laplace = cv2.Laplacian(img_blur, cv2.CV_64F)
end_time = cv2.getTickCount()
time_in_ms = (end_time - start_time) * 1000 / cv2.getTickFrequency()

# Output
print("Result")
print("--------------------------------------------------")
print ("Original")
cv2_imshow(img)
print ("Grayscale")
cv2_imshow(img_blur)
print("--------------------------------------------------")
print("Laplace")
cv2_imshow(laplace)

print("--------------------------------------------------")
print(f"Laplace edge detection took {time_in_ms:.2f} ms")