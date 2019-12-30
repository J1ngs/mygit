#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 24 09:50:52 2019

@author: Jing
"""

import os

def main(path1,path2):
    
#    names = os.listdir('./data/test/cloth')  #路径
    names = os.listdir(path1)  #路径

    i=0  #用于统计文件数量是否正确，不会写到文件里
    train_val = open(path2,'w')
    for name in names:
    #    index = name.rfind('.')
    #    name = name[:index]
        train_val.write(name+'\n')
        i=i+1
#    print(i)
        
def main2(path1,path2,path3):
    
    names1 = os.listdir(path1)  #路径
    names2 = os.listdir(path2)  #路径

    i=0  #用于统计文件数量是否正确，不会写到文件里
    train_val = open(path3,'w')
    for name1, name2 in zip(names1, names2):
    #    index = name.rfind('.')
    #    name = name[:index]
        train_val.write(name1+' '+name2)
        i=i+1
#    print(i)
        
        
        
if __name__ == "__main__":
    
    path1='./data/test/cloth'
    path2= './data/test/test.txt'
    main(path1,path2)
    
#    path1='./data/test/image'
#    path2='./data/test/cloth'
#    path3='./data/test_pairs.txt'
#    main2(path1, path2, path3)


