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
import test_GMM
import test_TOM
#import evaluate_parsing_JPPNet
import posetest
import t_text
import inference
import torch
from networks_parse import deeplab_xception_transfer, graph


img1 = os.path.abspath('data/test/cloth/001744_1.jpg') #文件名 001744_1 000218_1
imgc = cv2.imread(img1)
imgcn = os.path.basename(img1)
#plt.figure()
#plt.imshow(imgc)

img0 = os.path.abspath('data/test/image/000001_0.jpg') #文件名
imgh = cv2.imread(img0)
imghn = os.path.basename(img0)

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

net = deeplab_xception_transfer.deeplab_xception_transfer_projection_savemem(n_classes=20,
                                                                                 hidden_layers=128,
                                                                                 source_classes=7, )

x = torch.load('./checkpoints/universal_trained.pth')
net.load_source_model(x)

#imgpath = './img/messi.jpg' 
outputpath = './data/test/image-parse'
outputname = os.path.splitext(imghn)[0]

net.cuda()
use_gpu = True

inference.inference(net=net, img_path=img0 ,output_path=outputpath , output_name=outputname, use_gpu= use_gpu )


# =============================================================================
# pose generation
# =============================================================================

posetest.main(img0) #人像路径


# =============================================================================
# GMM
# =============================================================================

###testpairs.txt生成
path2='./data/test_pairs.txt'
train_val2 = open(path2,'w')
train_val2.write(imghn+' '+imgcn)
train_val2.close()

test_GMM.main()

# =============================================================================
# TOM
# =============================================================================

test_TOM.main()




