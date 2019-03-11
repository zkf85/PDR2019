# 2019/03/09
# rearrange dataset_for_keras and make a copy
import os
import json
import shutil
import utils

#===============================================================================
# 1. paths
#===============================================================================
base_dir = '/home/kefeng/data_pool/plant_disease_dataset'
source_dir = '/home/kefeng/data_pool/plant_disease_dataset/dataset_for_keras'
label_json = '../label_to_disease_full.json'

#===============================================================================
# Create directory for the new copy of dataset
#===============================================================================
dist_dir = os.path.join(base_dir, 'dataset_plant_categorical')
if not os.path.exists(dist_dir):
    os.mkdir(dist_dir)

#===============================================================================
# Load label json 
#===============================================================================
with open(label_json, 'r') as f:
    label_list = json.load(f)
label_dict = {}
for x in label_list:
    label_dict[x[0]] = x[1]

#===============================================================================
# Major Loop
#===============================================================================
subnames = ['concat', 'train', 'val']
for subname in subnames:
    count = 0
    source_subdir = os.path.join(source_dir, subname)
    dist_subdir =  os.path.join(dist_dir, subname)
    print('[KF INFO] Start copying in %s' % source_subdir)
    if not os.path.exists(dist_subdir):
        os.mkdir(dist_subdir)

    # Check source subsub names: '0', '1', ...
    subsubnames = sorted([f for f in os.listdir(source_subdir) if not f.startswith('.')])
    # Check source image files in subsubdirs
    for subsubname in subsubnames:
        cat_name = label_dict[int(subsubname)]
        source_subsubdir = os.path.join(source_dir, subname, subsubname)
        dist_subsubdir =  os.path.join(dist_dir, subname, cat_name)
        if not os.path.exists(dist_subsubdir):
            os.mkdir(dist_subsubdir)
        
        for f in os.listdir(source_subsubdir):
            if kfutils.is_image_file(f):
                s = os.path.join(source_subsubdir, f)
                d = os.path.join(dist_subsubdir, f)
                shutil.copy(s, d)
                count += 1
                if count % 100 == 0:
                    print('%s files are rearranged!' % count)

    print('[KF INFO] %s copying complete! %d files are copied in total!' % (subname, count))

