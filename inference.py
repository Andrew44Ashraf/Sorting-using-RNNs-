import os 
import sys 
from decoder_encoder import encode 
import tensorflow
from tensorflow.keras.models import load_model
import numpy as np 

testX = np.random.randint(100, size=(1, 10))
test = encode(testX, 10, 100)
model_loaded = load_model('sorting.h5')


predicted_sorted = model_loaded.predict(test,batch_size = 1)
print(testX)
print(np.sort(testX))
print(np.argmax(predicted_sorted, axis=2))