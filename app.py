import os
from flask import Flask, redirect, render_template, request, jsonify
from PIL import Image
import tensorflow as tf 
import numpy as np
import pandas as pd
import cv2
import csv



app = Flask(__name__)

soil_info = pd.read_csv(r'C:/Users/vedant raikar/Desktop/plantdisease/soil_data.csv',encoding='iso-8859-1', on_bad_lines='skip')

soil_type_model = tf.keras.models.load_model(r'C:/Users/vedant raikar/Desktop/plantdisease/converted_keras/keras_model.h5')


def soil_type(image_path):
    img = cv2.imread(image_path)
    img = cv2.resize(img, (224, 224))
    img = img.astype('float32') / 255.0
    img = np.expand_dims(img, axis=0)
    prediction = soil_type_model.predict(img)
      # list of possible soil type
    predicted_index = np.argmax(prediction)
    return predicted_index




@app.route('/')
def index():
     return render_template('index.html')


@app.route('/submit1', methods=['GET', 'POST'])
def submit():
    title = 0
    description = 0
   
    pred = 0
    data=0

    if request.method == 'POST':
        image_path = r'C:\Users\vedant raikar\Desktop\plantdisease\static\upload\10.jpg'
        pred = soil_type(image_path)
        with open(r'C:/Users/vedant raikar/Desktop/plantdisease/soil_data..csv', mode='r') as file:
         csv_reader = csv.DictReader(file)
         data = [row for row in csv_reader]
        title = soil_info['soil_name'][pred]
        description = soil_info['description'][pred]
      
    return render_template('submit1.html', title=title, desc=description,
                            pred=pred , data=data)




if __name__ == '__main__':
  app.run(debug=True)
  
