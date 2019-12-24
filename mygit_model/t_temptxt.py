#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 24 16:50:22 2019

@author: Jing
"""

import os
import cv2


img1 = os.path.abspath('data/000218_1.jpg') #文件名
imgc = cv2.imread(img1)
imgcn = os.path.basename(img1)

img0 = os.path.abspath('data/000001_0.jpg') #文件名
imgh = cv2.imread(img0)
imghn = os.path.basename(img0)


path1='./data/test/val.txt'
train_val1 = open(path1,'w')
train_val1.write(imghn+'\n')

path2='./data/test_pairs.txt'
train_val2 = open(path2,'w')
train_val2.write(imghn+' '+imgcn)