import numpy as np
import scipy.ndimage as ndimage
import matplotlib.pyplot as plt
#load a original image
img = ndimage.imread('image1.gif')
#print the image without make change or interpolation to it's pixel size
plt.imshow(img, interpolation='nearest')
plt.show()
# Set 0 for the last axis to not blur the color planes
# Set 5 for the first and second axis to build a 5*5 filter
# Convolute the matrix of original images and the 5*5 matrix for filter
img1 = ndimage.gaussian_filter(img, sigma=(5, 5, 0), order=0)
plt.imshow(img1, interpolation='nearest')
plt.show()
# Set 0 for the last axis to not blur the color planes
# Set 7 for the first and second axis to build a 7*7 filter
# Convolute the matrix of original images and the 7*7 matrix for filter
img1 = ndimage.gaussian_filter(img, sigma=(7, 7, 0), order=0)
plt.imshow(img1, interpolation='nearest')
plt.show()
# Set 0 for the last axis to not blur the color planes
# Set 9 for the first and second axis to build a 9*9 filter
# Convolute the matrix of original images and the 9*9 matrix for filter
img1 = ndimage.gaussian_filter(img, sigma=(9, 9, 0), order=0)
plt.imshow(img1, interpolation='nearest')
plt.show()


#code found from https://stackoverflow.com/questions/17595912/gaussian-smoothing-an-image-in-python
