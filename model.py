"""
Filename: model.py 
Created on Thu Mar 14 12:17:39 CST 2019

@author: Kefeng Zhu (zkf1985@gmail.com, zkf85@163.com)

Build model with given parameters.
"""
# Finetune Models
from tensorflow.keras import models
from tensorflow.keras import layers
from tensorflow.keras.applications import VGG16
from tensorflow.keras.applications import VGG19
from tensorflow.keras.applications import InceptionResNetV2 
from tensorflow.keras.applications import InceptionV3
from tensorflow.keras.applications import ResNet50

def build_model(model_name, img_size, num_classes):
    """
    Build model.

    Arguments
        model_name : (str) model name, which is used to select model.
        img_size : (int) image size for both width and height for modeling.
        num_classes : (int) number of classes for the last layer of the model.

    Returns
        model : a tensorflow model object.

    """
    image_shape = (img_size, img_size, 3)

    # Initialize model
    model = models.Sequential()

    # Load model
    if model_name == 'dummy':
        model.add(layers.MaxPooling2D(pool_size=(4, 4), input_shape=image_shape))

    else:
        print('[KF INFO] Loading pre-trained model ...')
        if model_name == 'VGG16':
            if img_size > 224:
                raise Exception("[KF ERROR] For %s model, the input image size cannot be larger than 224!" % model_name)
            conv = VGG16(weights='imagenet', include_top=False, input_shape=image_shape)
        elif model_name == 'VGG19':
            if img_size > 224:
                raise Exception("[KF ERROR] For %s model, the input image size cannot be larger than 224!" % model_name)
            conv = VGG19(weights='imagenet', include_top=False, input_shape=image_shape)
        elif model_name == 'InceptionResNetV2':
            if img_size > 299:
                raise Exception("[KF ERROR] For %s model, the input image size cannot be larger than 299!" % model_name)
            conv = InceptionResNetV2(weights='imagenet', include_top=False, input_shape=image_shape)
        elif model_name == 'InceptionV3':
            if img_size > 299:
                raise Exception("[KF ERROR] For %s model, the input image size cannot be larger than 299!" % model_name)
            conv = InceptionV3(weights='imagenet', include_top=False, input_shape=image_shape)
        elif model_name == 'ResNet50':
            if img_size > 224:
                raise Exception("[KF ERROR] For %s model, the input image size cannot be larger than 224!" % model_name)
            conv = ResNet50(weights='imagenet', include_top=False, input_shape=image_shape)
        else:
            raise Exception("[KF ERROR] Cannot load the pre-trained model! ")
        
        print("[KF INFO] The pretrained model %s's convolutional part is loaded ..." % model_name)
        model.add(conv)

    # Add top layers
    fc_size = 256
    model.add(layers.Flatten())
    model.add(layers.BatchNormalization())
    model.add(layers.Dense(fc_size, activation='relu'))
    model.add(layers.Dropout(0.5))
    model.add(layers.Dense(num_classes, activation='softmax'))

    return model


# Test
if (__name__ == "__main__"):
    print('*'*80) 
    print('Test %s' % __file__)
    print('*'*80) 
    model = build_model('dummy', 224, 10)
    model.summary()

