import tensorflow as tf
import keras 
from keras.preprocessing.image import ImageDataGenerator, img_to_array,array_to_img
import cv2
#import PIL
#from PIL.Image import load_img

datagen=ImageDataGenerator(
    rotation_range=-45,
    height_shift_range=0.3,
    zoom_range=0.5,
    vertical_flip=True,
    horizontal_flip=True,
    channel_shift_range=0.5    
    )

image=tf.keras.preprocessing.image.load_img('bugatti.jpg')
x=img_to_array(image)
x=x.reshape((1,)+x.shape)

i=0
for batch in datagen.flow(x, batch_size=2, save_to_dir="Data", save_format='png',save_prefix='car'):
    i=i+1
    if i==20:
        break;