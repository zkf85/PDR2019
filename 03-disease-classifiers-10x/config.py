"""
Filename: config.py
Created on Wed Mar 13 13:40:25 CST 2019

@author: Kefeng Zhu (zkf1985@gmail.com, zkf85@163.com)

Description:

"""
import os
import json

from utils import print_title, is_image_file
from datetime import datetime
from argparse import ArgumentParser

# Save current date/time
now = datetime.now()

# Add an argument representing the category to be processed. e.g. 'apple'
parser = ArgumentParser()
parser.add_argument('category_name', type=str)
args = vars(parser.parse_args())
category_name = args['category_name']

category_list = ('apple', 'cherry', 'citrus', 'corn', 'grape', 'peach', 'pepper', 'potato', 'strawberry', 'tomato')
if category_name not in category_list:
    raise Exception("[KF ERROR] The category name entered '{0}' is not valid!".format(category_name))

# Load 'cat-to-folders.json for assertion
with open('cat-to-folders.json', 'r') as f:
    cat_dic = json.load(f)
    print(cat_dic)

#===============================================================================
# Hyper-parameters:
#===============================================================================
epochs = 50
batch_size = 16
lr = 1e-4
early_stopping_patience = 20
lr_reduce_patience = 8

model_name, img_size = 'VGG16', 224
#model_name, img_size = 'VGG19', 224
#model_name, img_size = 'ResNet50', 224
#model_name, img_size = 'InceptionV3', 299
#model_name, img_size = 'InceptionResNetV2', 299
img_shape = (img_size, img_size, 3)

# Data paths:
base_data = '/home/kefeng/data_pool/plant_disease_dataset/dataset_for_10x_classifiers'
train_data = os.path.join(base_data, category_name, 'train')
assert os.path.exists(train_data)
val_data = os.path.join(base_data, category_name, 'val')
assert os.path.exists(val_data)

# Calculate train/val size and num_classes
cats = sorted([s for s in os.listdir(train_data) if not s.startswith('.')])
assert cat_dic[category_name] == cats

num_classes = len(cats)
train_size = 0
val_size = 0
for c in cats:
    train_size += len([i for i in os.listdir(os.path.join(train_data, c)) if is_image_file(i)])
    val_size += len([i for i in os.listdir(os.path.join(val_data, c)) if is_image_file(i)])


# Model save path:
model_base_dir = '/home/kefeng/model_pool/plant_disease_recognition_models/child_models'
if not os.path.exists(model_base_dir):
    os.mkdir(model_base_dir)
foldername = '%s-%d%02d%02d-%s-epochs-%d-batchsize-%d' % (category_name, now.year, now.month, now.day, model_name, epochs, batch_size)
model_save_dir = os.path.join(model_base_dir, foldername)
logfile = 'training_log.txt'

def print_params():
    print('Date/Time:')
    print('%d/%02d/%02d %02d:%02d:%02d' %(now.year, now.month, now.day, now.hour, now.minute, now.second))
    print_title('Training Parameters')
    print("Category         :", category_name)
    print("Model Saving Folder:")
    print('├─', foldername)
    print('-'*80)
    print("Model Name       :", model_name)
    print("Image Shape      :", img_shape)
    print('-'*80)
    print("Num of Classes   :", num_classes)
    print("Train Size       :", train_size)
    print("Validation Size  :", val_size)
    print('-'*80)
    print("Epochs           :", epochs)
    print("Batch Size       :", batch_size)
    print("Initial LR       :", lr)
    print("Early Stopping Patience  :", early_stopping_patience)
    print("LR Reduce Patience       :", lr_reduce_patience)
    print('-'*80)

def save_params_to_log():
    if not os.path.exists(model_save_dir):
        os.mkdir(model_save_dir)
    with open(os.path.join(model_save_dir, logfile), 'w') as f:
        print('Training logfile:', file=f)
        print('Logfile created on:', file=f)
        print('%d/%02d/%02d %02d:%02d:%02d' %(now.year, now.month, now.day, now.hour, now.minute, now.second), file=f)
        print_title('Training Parameters', f=f)
        print("Category         :", category_name, file=f)
        print("Model Saving Folder:", file=f)
        print('├─', foldername, file=f)
        print('-'*80, file=f)
        print("Model Name       :", model_name, file=f)
        print("Image Shape      :", img_shape, file=f)
        print('-'*80, file=f)
        print("Num of Classes   :", num_classes, file=f)
        print("Train Size       :", train_size, file=f)
        print("Validation Size  :", val_size, file=f)
        print('-'*80, file=f)
        print("Epochs           :", epochs, file=f)
        print("Batch Size       :", batch_size, file=f)
        print("Initial LR       :", lr, file=f)
        print("Early Stopping Patience  :", early_stopping_patience, file=f)
        print("LR Reduce Patience       :", lr_reduce_patience, file=f)
        print('-'*80, file=f)
    

#===============================================================================
# Test
#===============================================================================
if (__name__ == '__main__'):
    print_title('[KF INFO] Test config.py')
    print_params()
    #save_params_to_log()
    
