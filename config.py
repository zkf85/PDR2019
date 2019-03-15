"""
Filename: config.py
Created on Wed Mar 13 13:40:25 CST 2019

@author: Kefeng Zhu (zkf1985@gmail.com, zkf85@163.com)

== Plant Disease Recognition (PDR) ==
Read and preprocess the paramters.

"""
import os
import json
from argparse import ArgumentParser

from utils import print_title, is_image_file, category_list, cat_to_labels_dict  

# Add an argument representing the category to be processed. e.g. 'apple'
parser = ArgumentParser()
parser.add_argument('--category_name', required=True,
                    help='if "categorical" train categorical models, else, train child PDR models')
parser.add_argument('--date', required=True)
parser.add_argument('--epochs', required=True, type=int)
parser.add_argument('--batch_size', required=True, type=int)
parser.add_argument('--lr', required=True, type=float)
parser.add_argument('--early_stopping_patience', required=True, type=int)
parser.add_argument('--lr_reduce_patience', required=True, type=int)
parser.add_argument('--model_name', required=True)
parser.add_argument('--img_size', required=True, type=int)
parser.add_argument('--data_base_dir', required=True)
parser.add_argument('--model_save_dir', required=True)
# Load arguments as parameters
args = vars(parser.parse_args())

# Set parameters
category_name = args['category_name']
date = args['date']
epochs = args['epochs']
batch_size = args['batch_size']
lr = args['lr']
early_stopping_patience = args['early_stopping_patience']
lr_reduce_patience = args['lr_reduce_patience']
model_name = args['model_name']
img_size = args['img_size']
data_base_dir = args['data_base_dir']
model_save_dir = args['model_save_dir']

img_shape = (img_size, img_size, 3)

# Categorical Models' Path
if category_name == 'categorical':
    train_data_dir = os.path.join(data_base_dir,'train')
    val_data_dir = os.path.join(data_base_dir, 'val')
    assert os.path.exists(train_data_dir) and os.path.exists(val_data_dir)

    cats = sorted([s for s in os.listdir(train_data_dir) if not s.startswith('.')])
    assert category_list == cats
    
# Children PDR Models' Path
else:
    if category_name not in category_list:
        raise Exception("[KF ERROR] The category name entered '{0}' is not valid!".format(category_name))
    train_data_dir = os.path.join(data_base_dir, category_name, 'train')
    val_data_dir = os.path.join(data_base_dir, category_name, 'val')
    assert os.path.exists(train_data_dir) and os.path.exists(val_data_dir)

    cats = sorted([s for s in os.listdir(train_data_dir) if not s.startswith('.')])
    assert cat_to_labels_dict[category_name] == cats

# Calculate train/val size and num_classes
num_classes = len(cats)
train_size, val_size = 0, 0
for c in cats:
    train_size += len([i for i in os.listdir(os.path.join(train_data_dir, c)) if is_image_file(i)])
    val_size += len([i for i in os.listdir(os.path.join(val_data_dir, c)) if is_image_file(i)])

# Save file names:
prefix = '-'.join([date, category_name, model_name])
class_indices_filename = '%s-class-indices.json' % category_name
plt_acc_loss_filename = '-'.join([prefix, 'plt-acc-loss.eps'])
plt_lr_filename = '-'.join([prefix, 'plt-lr.eps'])
history_filename = 'history.json'
model_filename = 'model-' + os.path.split(model_save_dir)[-1] + '.hdf5'

def print_params():
    """
    Print parameters.
    """
    print("Category         :", category_name)
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
    print('Train Data Path‘ :')
    print(train_data_dir)
    print('Val Data Path‘   :')
    print(val_data_dir)
    print("Model Save Path  :")
    print(model_save_dir)
    
# Tests
if (__name__ == '__main__'):
    print_title('Test %s' % __file__, symbol='*')
    print_params()
    
