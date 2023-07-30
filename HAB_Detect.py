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
        if predictVal > 0.5: 
            print('Predicted class has an HAB {}'.format(image_path))
        else:
            print('Predicted class does not have a HAB {}'.format(image_path))