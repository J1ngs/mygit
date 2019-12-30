#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 01:08:22 2019

@author: Jing
"""
#用openpose模型跑出结果 并将其存储成固定的json格式
import sys
sys.path.insert(0, 'python')
import cv2
import model_pose
import util
from body import Body
import matplotlib.pyplot as plt
import copy
import numpy as np
import json
import os


def main(test_image):#path
    body_estimation = Body('model_pose/body_pose_model.pth')
    
#    test_image = 'images/9193.jpg'#demo.png
    oriImg = cv2.imread(test_image)  # B,G,R order
    
    candidate, subset = body_estimation(oriImg)
    
    #关键点显示
#    ca=candidate[:,0:2];
#    plt.subplot(1,2,1);
#    plt.plot(ca[:,0],ca[:,1],"ro")
#    plt.xlim((0, 191))
#    plt.ylim((0, 255))
#    plt.show()
    
    ##对得到的数据candidate&subset进行处理得到pose数据可用
    pose=np.zeros((18,3))
    sub1=subset[:,0:18];
    sub1=sub1.astype(int);
    ind=(sub1>-1);
    ind=ind.flatten();
    #pose[ind,:]=candidate[sub1[:,ind],0:3];
    pose[ind,:]=candidate[:,0:3];#上面一句的替代 更简洁
    pose=pose.reshape(-1,1);
    pose=pose.flatten();
    pose=pose.tolist()
    
    #生成字典
    posefile = {'people': [{'pose_keypoints':[]}]};
    posefile['people'][0]['pose_keypoints']=pose;
    
    name=os.path.basename(test_image)
    name=name.replace('.jpg', '_keypoints.json')
    path=os.path.join('./data/test/pose',name)

    #save as json
    with open(path,'w') as file_obj:
        json.dump(posefile,file_obj)
        
        


