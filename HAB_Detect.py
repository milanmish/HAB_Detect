import os
import shutil
import tensorflow as tf
import numpy as np
import cv2
from keras.models import load_model

source_folder = r"D:\DCIM\100MEDIA\\"
destination_folder = r"C:\Users\25milanbm\Desktop\HAB_Detect\drone_data\\"

if os.path.isfile(source_folder):

    for file_name in os.listdir(source_folder):
        source = source_folder + file_name
        if os.path.isfile(source):
            destination = destination_folder + file_name
            shutil.copy(source, destination)

HAB_Detect = load_model('models/hab_detect.keras')
data_dir = "drone_data"

for image in os.listdir(data_dir):
    image_path = os.path.join(data_dir, image)
    img = cv2.imread(image_path)
    resize = tf.image.resize(img, (256,256))
    predictVal = HAB_Detect.predict(np.expand_dims(resize/255, 0))
    if predictVal > 0.5: 
        print('Predicted class likely has an algae bloom {}'.format(image_path))
        with open('pab.txt', 'a') as f:
            f.write(image_path  + str(predictVal) + '\n')
    else:
        print('Predicted class likely does not have an algae bloom {}'.format(image_path))
        with open('npab.txt', 'a') as f:
            f.write(image_path  + str(predictVal) + '\n')