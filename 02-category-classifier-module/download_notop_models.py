from tensorflow.keras.applications import VGG16
from tensorflow.keras.applications import VGG19
from tensorflow.keras.applications import InceptionResNetV2
from tensorflow.keras.applications import InceptionV3


s1 = (224,224,3)
s2 = (299,299,3)

conv = VGG16(weights='imagenet', include_top=False, input_shape=s1)
conv = VGG19(weights='imagenet', include_top=False, input_shape=s1)
conv = InceptionResNetV2(weights='imagenet', include_top=False, input_shape=s2)
conv = InceptionV3(weights='imagenet', include_top=False, input_shape=s2)

