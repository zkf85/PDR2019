"""
Filename: predict.py 
Created on Fri Mar 15 11:26:47 CST 2019

@author: Kefeng Zhu (zkf1985@gmail.com, zkf85@163.com)

== Plant Disease Recognition (PDR) ==
Predict

"""
import os
import json
import numpy as np
import time
#from argparse import ArgumentParser                                                                                               
# To Force using CPU
os.environ["CUDA_DEVICE_ORDER"] = "PCI_BUS_ID"   # see issue #152
os.environ["CUDA_VISIBLE_DEVICES"] = ""

from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array
import tensorflow as tf

def get_imgsize_from_path(model_path):
    """
    Get image size from model's path

    Arguments
        model_path : (str) model file (hdf5) full path

    Returns
        img_size : (int) image size
    """
    return int(os.path.split(model_path)[-1].split('imgsize-')[1].split('-')[0])


def predict(model, graph, img_size, class_indices_path, image_path):
    """
    Predict

    Arguments
        class_indices_path : (str) class indices file  full path
        image_path : (str) test images path

    Returns
        prediected_label : (str) the predicted label based on class_indices

    """
    print(os.path.split(image_path)[-1])
    img_shape = (img_size, img_size, 3)

    # Get index to class label dictionary
    with open(class_indices_path, 'r') as f:
        class_indices = json.load(f)
        indices_class = {v: k for k, v in class_indices.items()}
    
    img = load_img(image_path, target_size=img_shape)
    img_np = img_to_array(img)/255.0
    img_np = np.expand_dims(img_np, axis=0)
    with graph.as_default():
        print('[KF INFO] Start predicting ...')
        proba = model.predict(img_np, verbose=1)[0]
        sorted_idx = np.argsort(proba)
        predicted_label = indices_class[sorted_idx[-1]]
        print(predicted_label)

    return predicted_label


# Test
if __name__ == "__main__":
    cat_model_path = '/home/kefeng/model_pool/plant_disease_recognition_models/categorical_models/20190312-model-InceptionResNetV2-epochs-20-batchsize-8/model-categorical-20190312-InceptionResNetV2-imgsize-299-epochs-20-batchsize-8.hdf5'
    cat_class_indices_path = '/home/kefeng/model_pool/plant_disease_recognition_models/categorical_models/20190312-model-InceptionResNetV2-epochs-20-batchsize-8/categorical-class-indices.json'
    apple_model_path = '/home/kefeng/model_pool/plant_disease_recognition_models/child_models/apple-20190313-VGG16-imgsize-224-epochs-50-batchsize-16/model-apple-20190313-VGG16-imgsize-224-epochs-50-batchsize-16.hdf5'
    apple_class_indices_path = '/home/kefeng/model_pool/plant_disease_recognition_models/child_models/apple-20190313-VGG16-imgsize-224-epochs-50-batchsize-16/apple-class-indices.json'

    cat_model_path_2 = '/home/kefeng/model_pool/plant_disease_recognition_models/categorical_models/20190313-model-VGG16-epochs-20-batchsize-8/model-categorical-20190313-VGG16-imgsize-224-epochs-20-batchsize-8.hdf5'
    cat_class_indices_path_2 = '/home/kefeng/model_pool/plant_disease_recognition_models/categorical_models/20190313-model-VGG16-epochs-20-batchsize-8/categorical-class-incdices.json'


    test_image_dir = '/home/kefeng/data_pool/plant_disease_dataset/dataset_for_keras/val/1'
    files = [f for f in os.listdir(test_image_dir) if f.rsplit('.',1)[1].lower() in ('jpg', 'png', 'jpeg') and not f.startswith('.')]

    print('[KF INFO] Loading models ...')
    start = time.time()
    cat_model = load_model(cat_model_path)
    cat_imgsize = get_imgsize_from_path(cat_model_path)

    cat_model_2 = load_model(cat_model_path_2)
    cat_imgsize_2 = get_imgsize_from_path(cat_model_path_2)

    apple_model = load_model(apple_model_path)
    apple_imgsize = get_imgsize_from_path(apple_model_path)

    g = tf.get_default_graph()
    print('[KF INFO] Models are loaded!')
    print('[KF INFO] Time spent :', time.time() - start)

    for f in files[:5]:
        predict(cat_model, g, cat_imgsize, cat_class_indices_path, os.path.join(test_image_dir, f))
        predict(cat_model_2, g, cat_imgsize_2, cat_class_indices_path_2, os.path.join(test_image_dir, f))
        predict(apple_model, g, apple_imgsize, apple_class_indices_path, os.path.join(test_image_dir, f))

