import tensorflow 
import keras
from keras.models import Sequential

from keras.layers.core import Activation, RepeatVector,  Dropout, Dense
from keras.layers import recurrent
import numpy as np
from decoder_encoder import batch_gen, encode
RNN = recurrent.LSTM


batch_size=32
seq_len = 10
max_no = 100


model = Sequential()
model.add(RNN(100, input_shape=(seq_len, max_no)))


model.add(Dropout(0.25))
#model.add(Dropout(0.012))


model.add(RepeatVector(seq_len))
model.add(RNN(100, return_sequences=True))
model.add(Dense(max_no))
model.add(Dropout(0.5))
model.add(Activation('softmax'))

model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

print (model.summary)


for ind,(X,Y) in enumerate(batch_gen(batch_size, seq_len, max_no)):
    loss, acc = model.train_on_batch(X, Y)
    # We'll test RNN after each 250 iteration to check how well it is performing
    if ind % 250 == 0:
        testX = np.random.randint(max_no, size=(1, seq_len))
        test = encode(testX, seq_len, max_no)
        print (testX)
      
        y = model.predict(test, batch_size=1)
     
        print (np.sort(testX))


model.save("sorting.h5")
