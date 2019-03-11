# Created by KF
# 2019/03/11

# Finetune Models
from tensorflow.keras import models
from tensorflow.keras import layers
#from tensorflow.keras.applications import VGG16
#from tensorflow.keras.applications import VGG19
from tensorflow.keras.applications import InceptionResNetV2 
from tensorflow.keras.applications import InceptionV3
from tensorflow.keras.applications import ResNet50

def build_model(model_name, img_size, num_classes):
    image_shape = (img_size, img_size, 3)

    # Load model
    print('[KF INFO] Loading pre-trained model ...')
    if model_name == 'VGG16':
        if img_size != 224:
            raise("[KF ERROR] For %s model, the input image size is not 224!" % model_name)
        conv = VGG16(weights='imagenet', include_top=False, input_shape=img_shape)
    elif model_name == 'VGG19':
        if img_size != 224:
            raise("[KF ERROR] For %s model, the input image size is not 224!" % model_name)
        conv = VGG19(weights='imagenet', include_top=False, input_shape=image_shape)
    elif model_name == 'InceptionResNetV2':
        if img_size != 299:
            raise("[KF ERROR] For %s model, the input image size is not 299!" % model_name)
        conv = InceptionResNetV2(weights='imagenet', include_top=False, input_shape=image_shape)
    elif model_name == 'InceptionV3':
        if img_size != 299:
            raise("[KF ERROR] For %s model, the input image size is not 299!" % model_name)
        conv = InceptionV3(weights='imagenet', include_top=False, input_shape=image_shape)
    elif model_name == 'ResNet50':
        if img_size != 224:
            raise("[KF ERROR] For %s model, the input image size is not 224!" % model_name)
        conv = ResNet50(weights='imagenet', include_top=False, input_shape=image_shape)
    else:
        raise("[KF INFO] Cannot load the pre-trained model! ")

    print("[KF INFO] The pretrained model %s's convolutional part is loaded ..." % model_name)
    model = models.Sequential()
    model.add(conv)

    # Add top layers
    model.add(layers.Flatten())
    model.add(layers.BatchNormalization())
    model.add(layers.Dense(1024, activation='relu'))
    model.add(layers.Dropout(0.5))
    model.add(layers.Dense(num_classes, activation='softmax'))

    return model


if (__name__ == "__main__"):
    print('-'*80)
    print('[KF INFO] Test models.py')
    print('-'*80)

    model = build_model('ResNet50', 224, 10)
    
    model.summary()
