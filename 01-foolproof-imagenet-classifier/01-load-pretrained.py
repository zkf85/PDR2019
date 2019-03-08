###############################################################################
# 01. Fool Proof Classifier
#   Applying a pretrained imagenet-based classifier. e.g. Inception.
#
# KF 03/08/2019
################################################################################
import numpy as np
import os
import json
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array

#===============================================================================
# Load Model
#===============================================================================
# InceptionV3
img_shape = (299, 299, 3)
#from tensorflow.keras.applications import InceptionV3 
#model = InceptionV3(weights='imagenet', include_top=True)
#model.save('inception_v3_1000.h5')

model_path = '~/model_pool/plant_disease_recognition_models/inception_v3_1000.h5'
model = load_model(model_path)

#===============================================================================
# Predict
#===============================================================================
# Test image file names:
test_dir = 'general-test-images'
test_files = [i for i in os.listdir(test_dir) if not i.startswith('.')]

# Load human readable imagenet labels txt file:
imagenet_label_file = 'imagenet1000_clsidx_to_labels.txt'

with open(imagenet_label_file, 'r') as f:
    # evaluate txt file content as dictionary
    imagenet_label_dict = eval(f.read())

# Test Loop:
plant_dict = {}
for f in sorted(test_files):
    print('-'*80)
    print('test_file:', f)
    img = load_img(os.path.join(test_dir, f), target_size=img_shape)
    img_np = img_to_array(img)
    img_np = img_np / 255.0
    img_np = np.expand_dims(img_np, axis=0)

    proba = model.predict(img_np, verbose=1)[0]
    print('confidence:', max(proba))
    res_idx = np.argmax(proba)
    print('predicted index:', res_idx)
    print('predicted class:', imagenet_label_dict[res_idx])
    if max(proba) > 0.2:
        plant_dict[str(res_idx)] = imagenet_label_dict[res_idx]

with open('imagenet_plants.json', 'w') as f:
    json.dump(plant_dict, f, indent=4)

   

