# Created by KF
# 2019/03/11

# Train the categorical Model
import os
from tensorflow.keras import optimizers
from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.preprocessing.image import ImageDataGenerator

from sklearn.preprocessing import LabelBinarizer

import config
from utils import print_title
from model import build_model


print_title("PDR - Train Categorical Classifier")


# Build model
print_title("I. Build Model")
model = build_model(config.model_name, config.img_size, config.num_classes)

optimizer = optimizer.Adam(lr=config.lr)
model.compile(optimizer=optimizer,
            loss='categorical_crossentropy',
            metrics=['accuracy']
            )

model.summary()

# Callbacks

