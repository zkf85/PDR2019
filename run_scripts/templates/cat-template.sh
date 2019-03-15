#!/bin/bash
#===============================================================================
# Created on Thu Mar 14 15:15:15 CST 2019
#
# @author: Kefeng Zhu (zkf1985@gmail.com, zkf85@163.com)
#
#===============================================================================
date=`date +%Y%m%d`

# Hyper-parameters
epochs=2
batch_size=16
lr="1e-4"
early_stopping_patience=20
lr_reduce_patience=8

model_name="dummy"; img_size=224
#model_name="VGG16"; img_size=224
#model_name="VGG19"; img_size=224
#model_name="InceptionResNetV2"; img_size=299
#model_name="InceptionV3"; img_size=299
#model_name="ResNet50"; img_size=224

# Paths
category_name="categorical"
data_base_dir="/home/kefeng/data_pool/plant_disease_dataset/dataset_plant_categorical"
model_base_dir="/home/kefeng/model_pool/plant_disease_recognition_models/categorical_models"
model_save_dir="$model_base_dir/$category_name-$date-$model_name-imgsize-$img_size-epochs-$epochs-batchsize-$batch_size"
mkdir -p $model_save_dir
logfile_path="$model_save_dir/train_log.out"

script_dir="/home/kefeng/2019-PlantDiseaseRecognition-v2"
script_path="$script_dir/train.py"
#script_path="$script_dir/config.py"

# Run
python $script_path \
--category_name      $category_name \
--date               $date \
--epochs             $epochs \
--batch_size         $batch_size \
--lr                 $lr \
--early_stopping_patience    $early_stopping_patience \
--lr_reduce_patience         $lr_reduce_patience \
--model_name         $model_name \
--img_size           $img_size \
--data_base_dir      $data_base_dir \
--model_save_dir     $model_save_dir \
#> $logfile_path

plots_dir="$script_dir/02-category-classifier-module/plots"
cp $model_save_dir/*.eps $plots_dir
