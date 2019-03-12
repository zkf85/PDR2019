################################################################################
# Created by KF
# 2019/03/11
# Configuration - parameters
################################################################################
import os
from utils import print_title
from datetime import datetime
now = datetime.now()

#===============================================================================
# Hyper-parameters:
#===============================================================================
epochs = 20
batch_size = 8
lr = 1e-4
early_stopping_patience = 30
lr_reduce_patience = 10

#model_name, img_size = 'VGG19', 224
#model_name, img_size = 'ResNet50', 224
#model_name, img_size = 'InceptionV3', 299
model_name, img_size = 'InceptionResNetV2', 299
img_shape = (img_size, img_size, 3)

train_size = 31718
val_size = 4540
num_classes = 10

#===============================================================================
# Paths:
#===============================================================================
train_data = '/home/kefeng/data_pool/plant_disease_dataset/dataset_plant_categorical/train'
val_data = '/home/kefeng/data_pool/plant_disease_dataset/dataset_plant_categorical/val'

model_base_dir = '/home/kefeng/model_pool/plant_disease_recognition_models/'
foldername = '%d%02d%02d-model-%s-epochs-%d-batchsize-%d' % (now.year, now.month, now.day, model_name, epochs, batch_size)
model_save_dir = os.path.join(model_base_dir, foldername)
logfile = 'training_log.txt'

def print_params():
    print('Date/Time:')
    print('%d/%02d/%02d %02d:%02d:%02d' %(now.year, now.month, now.day, now.hour, now.minute, now.second))
    print_title('Training Parameters')
    print("Model Saving Folder:")
    print('├─', foldername)
    print('-'*80)
    print("Model Name       :", model_name)
    print("Image Shape      :", img_shape)
    print('-'*80)
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
        print("Model Saving Folder:", file=f)
        print('├─', foldername, file=f)
        print('-'*80, file=f)
        print("Model Name       :", model_name, file=f)
        print("Image Shape      :", img_shape, file=f)
        print('-'*80, file=f)
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
    save_params_to_log()
    

