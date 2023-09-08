import os
import tensorflow as tf
import numpy as np
import cv2
from keras.models import load_model

HAB_Detect = load_model('models/hab_detect.keras')
data_dir = 'data'

for image_class in os.listdir(data_dir): 
    for image in os.listdir(os.path.join(data_dir, image_class)):
        image_path = os.path.join(data_dir, image_class, image)
        img = cv2.imread(image_path)
        resize = tf.image.resize(img, (256,256))
        predictVal = HAB_Detect.predict(np.expand_dims(resize/255, 0))
        if predictVal > 0.45: 
            print('Predicted class likely has an algae bloom {}'.format(image_path))
            with open('pab.txt', 'a') as f:
                f.write(image_path + '\n')
        else:
            print('Predicted class likely does not have an algae bloom {}'.format(image_path))
            with open('npab.txt', 'a') as f:
                f.write(image_path + '\n')