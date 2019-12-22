#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 21 17:05:38 2019

@author: Jing
"""

import cv2
import numpy as np
import scipy as sp
import scipy.ndimage
from scipy import signal
import matplotlib.pyplot as plt

def flood_fill(test_array,h_max=255):
    input_array = np.copy(test_array) 
    el = sp.ndimage.generate_binary_structure(2,2).astype(np.int)
    inside_mask = sp.ndimage.binary_erosion(~np.isnan(input_array), structure=el)
    output_array = np.copy(input_array)
    output_array[inside_mask]=h_max
    output_old_array = np.copy(input_array)
    output_old_array.fill(0)   
    el = sp.ndimage.generate_binary_structure(2,1).astype(np.int)
    while not np.array_equal(output_old_array, output_array):
        output_old_array = np.copy(output_array)
        output_array = np.maximum(input_array,sp.ndimage.grey_erosion(output_array, size=(3,3), footprint=el))
    return output_array

img = cv2.imread("000218_1.jpg");

a1=img[:,:,0]<250;
a2=img[:,:,1]<250;
a3=img[:,:,2]<250;
img= a1&a2&a3;

img=flood_fill(img);
img=img.astype(float);

for i in range(3,10,2):
    img = signal.medfilt(img,i)
    plt.subplot(2,2,(i-1)/2);
#    plt.figure()
    plt.imshow(img)
    
print('hello')



# =============================================================================
# 第二种imfill方法
# =============================================================================

#import cv2;
#import numpy as np;
# 
## Read image
#im_in = cv2.imread("nickel.jpg", cv2.IMREAD_GRAYSCALE);
# 
## Threshold.
## Set values equal to or above 220 to 0.
## Set values below 220 to 255.
# 
#th, im_th = cv2.threshold(im_in, 220, 255, cv2.THRESH_BINARY_INV);
# 
## Copy the thresholded image.
#im_floodfill = im_th.copy()
# 
## Mask used to flood filling.
## Notice the size needs to be 2 pixels than the image.
#h, w = im_th.shape[:2]
#mask = np.zeros((h+2, w+2), np.uint8)
# 
## Floodfill from point (0, 0)
#cv2.floodFill(im_floodfill, mask, (0,0), 255);
# 
## Invert floodfilled image
#im_floodfill_inv = cv2.bitwise_not(im_floodfill)
# 
## Combine the two images to get the foreground.
#im_out = im_th | im_floodfill_inv
# 
## Display images.
#cv2.imshow("Thresholded Image", im_th)
#cv2.imshow("Floodfilled Image", im_floodfill)
#cv2.imshow("Inverted Floodfilled Image", im_floodfill_inv)
#cv2.imshow("Foreground", im_out)
