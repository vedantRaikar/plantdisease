import cv2
import numpy as np
from tensorflow import keras

# Load the pre-trained Keras model
model = keras.models.load_model(r'C:\Users\vedant raikar\Desktop\plantdisease\soil type dataset\converted_keras\keras_model.h5')

# Load and resize the input image
img = cv2.imread(r'C:\Users\vedant raikar\Desktop\plantdisease\images\images.jpg')
# resize to match the input size of the model
img = cv2.resize(img, (224, 224))
img = img.astype('float32') / 255.0  # normalize pixel values to range [0, 1]

# Add an extra dimension to match the input shape expected by the model
img = np.expand_dims(img, axis=0)

# Make a prediction using the Keras model
prediction = model.predict(img)

# Get the predicted soil type from the output probabilities
soil_types = ['black soil', 'clinder soil', 'laterite soil','peat soil' ,'yellow soil']  # list of possible soil types
predicted_index = np.argmax(prediction)
predicted_soil_type = soil_types[predicted_index]

# Print the predicted soil type
print('The predicted soil type is:', predicted_soil_type)
