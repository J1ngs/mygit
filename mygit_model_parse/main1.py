#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 21 20:43:17 2019

@author: Jing
"""

import cv2
import os
import matplotlib.pyplot as plt

import t_mask
#import test_GMM
#import test_TOM
import evaluate_parsing_JPPNet
import posetest
import t_text

img = os.path.abspath('data/000218_1.jpg') #文件名
imgc = cv2.imread(img)
imgcn = os.path.basename(img)
#plt.figure()
#plt.imshow(imgc)

img = os.path.abspath('data/000001_0.jpg') #文件名
imgh = cv2.imread(img)

# =============================================================================
# mask generation
# =============================================================================

mask=t_mask.main(imgc)
mask=mask*255

#保存到指定路径

cv2.imwrite("./data/test/cloth-mask/{}".format(imgcn), mask)

###debug
#img = os.path.abspath('data/test/cloth-mask/000218_1.jpg') #文件名
#imgc = cv2.imread(img)
#plt.figure()
#plt.imshow(imgc)

# =============================================================================
# parse generation
# =============================================================================
# val.txt生成
path1='./data/test/image'
path2='./data/test/val.txt'
t_text.main(path1, path2)

#保存到指定路径 仅保存单通道parse
evaluate_parsing_JPPNet.main() #生成了图像 存入指定路径


# =============================================================================
# pose generation
# =============================================================================

posetest.main(img) #人像路径


# =============================================================================
# GMM
# =============================================================================

###testpairs.txt生成
path1='./data/test/image'
path2='./data/test/cloth'
path3='./data/test_pairs.txt'
t_text.main2(path1, path2, path3)

#test_GMM.main()

# =============================================================================
# TOM
# =============================================================================

#test_TOM.main()




