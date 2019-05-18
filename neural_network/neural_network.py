from __future__ import absolute_import, division, print_function, unicode_literals

import numpy as np
import pandas as pd

import tensorflow as tf

from tensorflow import feature_column
from tensorflow.keras import layers
from sklearn.model_selection import train_test_split

from tensorflow import keras


# read data file
# shuffle the rows since we had removed some columns and rows
# to achieve better accuracy
data = pd.read_csv('men_dataset.csv', na_values=['.'])
data = data.sample(frac=1)
# separate the output data (column 'num') from rest of the data
values_series = data['winner']
x_data = data.pop('winner')
for i in ["id1", "name1", "id2", "name2", "match"]:
    data.pop(i)
# print(x_data)

# split input(x) and output (y) data
# for training and testing
train_x_data = data[0:64]
train_y_data = x_data[0:64]
train_x_data = train_x_data.values
train_y_data = train_y_data.values

test_x_data = data[64:]
test_y_data = x_data[64:]
test_x_data = test_x_data.values
test_y_data = test_y_data.values

# create model
model = keras.Sequential()

print(train_x_data)
print("Shape {}".format(train_x_data.shape[1]))
# add layers
model.add(keras.layers.Dense(10, activation=tf.nn.relu, input_shape=(train_x_data.shape[1],)))
model.add(keras.layers.Dense(64, activation=tf.nn.relu))
model.add(keras.layers.Dense(32, activation=tf.nn.relu))
model.add(keras.layers.Dense(16, activation=tf.nn.relu))

# last layer has only two possible outcomes
# either 0 or 1 indicating not diagnosed and diagnosed respectively
model.add(keras.layers.Dense(1, activation=tf.nn.sigmoid))

# get summary of the model
model.summary()

model.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy'])

# model fitting, we train and test the data
history = model.fit(train_x_data,
                    train_y_data,
                    epochs=750,
                    batch_size=256,
                    validation_data=(test_x_data, test_y_data),
                    verbose=1)

loss, accuracy = model.evaluate(test_x_data, test_y_data)
print("Accuracy", accuracy)
print(model.predict(pd.DataFrame.from_dict({"ranking": [0.8], "surface": [0.35], "previous": [0.5]})))

model.save("my_model.h5")
