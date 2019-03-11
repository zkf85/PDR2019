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
batch_size = 64
lr = 1e-4
#img_size = 299
img_size = 224
img_shape = (img_size, img_size, 3)
num_classes = 10

#===============================================================================
# Paths:
#===============================================================================
train_data = '/home/kefeng/data_pool/plant_disease_dataset/dataset_plant_categorical/train'
val_data = '/home/kefeng/data_pool/plant_disease_dataset/dataset_plant_categorical/val'
model_name = 'ResNet50'

model_base_dir = '/home/kefeng/model_pool/plant_disease_recognition_models/'
model_save_dir = os.path.join(model_base_dir, '%d%02d%02d-model-%s-epochs-%d-batchsize-%d' % (now.year, now.month, now.day, model_name, epochs, batch_size))


#===============================================================================
# Test
#===============================================================================
if (__name__ == '__main__'):
    print('-'*80)
    print('[KF INFO] Test config.py')
    print('-'*80)
    print('model_save_dir:', model_save_dir)


