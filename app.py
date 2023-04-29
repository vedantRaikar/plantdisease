from flask import Flask , request , jsonify , render_template , redirect ,url_for
import tensorflow as tf 
import numpy as np 
from PIL import Image
import pickle 
import cv2 
from tensorflow import keras 
import torchvision.transforms.functional as TF
import CNN  
import torch
import os 




app = Flask(__name__)

disease_prediction_model = torch.load('model_path' , map_location=torch.device('cpu'))
soil_type_model= keras.models.load_model(r'')

def soil_type(image_path):
    img = cv2.imread(image_path)
    img = cv2.resize(img, (224, 224))
    img = img.astype('float32') / 255.0
    img = np.expand_dims(img, axis=0)
    prediction = soil_type_model.predict(img)
    soil_types = ['black soil', 'clinder soil', 'laterite soil','peat soil', 'yellow soil']  # list of possible soil type
    predicted_index = np.argmax(prediction)
    predicted_soil_type = soil_types[predicted_index]
    return predicted_soil_type
    


def disease_predict(image_path):
     image = Image.open(image_path).convert('RGB')
     image = image.resize((224,224))
     image = np.array(image).astype(np.float32)/255.0
     image = np.transpose(image, (2, 0, 1))
     image = torch.from_numpy(image)
     image = image.unsqueeze(0)
     prediction = disease_prediction_model(image)
     disease_labels = ['healthy', 'disease1', 'disease2']
     predicted_index = torch.argmax(prediction, dim=1)
     predicted_label = disease_labels[predicted_index]
     return predicted_label




@app.route('/home', method = ['POST', 'GET'])
def home():
 if request.method == 'POST':
     if request.form.get('home') == 'value1':
       return redirect(url_for('index'))
     elif request.form.get('about') == 'value2':
       return redirect(url_for('about'))
     elif request.form.get('agriculture') == 'val3':
       return redirect(url_for('agriculture'))
     elif request.form.get('contact') == 'val4':
       return redirect(url_for('contact'))

 elif request.method == 'GET':
    return render_template('home.html')



@app.route('/agriculture' , method= ['POST' , 'GET'])
def agriculture():
 if request.method == 'POST':
    if request.form.get('submit soil') == 'VAL1':
      return redirect(url_for('soil'))
    elif request.form.get('submit disease') == 'VAL2':
      return redirect(url_for('disease'))
 elif request.method == 'GET':
     return render_template('agriculture')
 


@app.route('/predictingsoil' , method=['POST' , 'GET'])
def soil():
   if request.method == 'POST':
      file_path = request.form('file_path')
      pred = soil_type(file_path)
      return render_template('result.html' , predicted_label = pred)
   

@app.route('/predictdisease', method=['POST', 'GET'])
def soil():
   if request.method == 'POST':
      file_path = request.form('file_path')
      pred = disease_predict(file_path)
      return render_template('result.html', predicted_label=pred)
   

      
  if __name__ == '__main__':
  app.run(port=5000 ,debug = True)