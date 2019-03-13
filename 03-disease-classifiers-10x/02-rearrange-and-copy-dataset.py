"""
Filename: 02-rearrange-and-copy-dataset.py 
Created on Wed Mar 13 11:16:09 CST 2019

@author: Kefeng Zhu (zkf1985@gmail.com, zkf85@163.com)

Description:
  Rearrange and copy the dataset.
  To facilitate keras.flow_from_directory, which will automatically detect all subfolders in the input 
  directory as categories.

  - load 'cat-to-folders.json', which is generated from 01....py

"""
import os
import json
from shutil import copytree
with open('cat-to-folders.json', 'r') as f:
    dic = json.load(f)

base_dir = '/home/kefeng/data_pool/plant_disease_dataset/dataset_for_keras'
dist_dir = '/home/kefeng/data_pool/plant_disease_dataset/dataset_for_10x_classifiers'
if not os.path.exists(dist_dir):
    os.mkdir(dist_dir)

subnames = ['concat', 'train', 'val']

for k, v in dic.items():
    dist_subdir = os.path.join(dist_dir, k)         # dist_subdir: dataset_for_10x_classifiers/apple
    if not os.path.exists(dist_subdir):
        os.mkdir(dist_subdir)
    for subname in subnames:
        subdir = os.path.join(base_dir, subname)    # subdir: dataset_for_keras/concat
        dist_subsubdir = os.path.join(dist_subdir, subname)     # dist_subsubdir: ~/apple/concat
        if not os.path.exists(dist_subdir):
            os.mkdir(dist_subdir)
        print(k, v)
        for i in v:
            subsubdir = os.path.join(subdir, i)    
            dist_subsubsubdir = os.path.join(dist_subsubdir, i)
            print('From:', subsubdir, os.path.exists(subsubdir))
            print('To:', dist_subsubsubdir)
            copytree(subsubdir, dist_subsubsubdir)

        
        

            



