from __future__ import absolute_import, division, print_function, unicode_literals

import pandas as pd
import tensorflow as tf
from tensorflow import keras


if __name__ == "__main__":
    data = pd.read_csv('women_dataset.csv', na_values=['.'])
    data = data.sample(frac=1)

    values_series = data['winner']
    x_data = data.pop('winner')
    for i in ["id1", "name1", "id2", "name2", "match"]:
        data.pop(i)

    train_x_data = data[0:64]
    train_y_data = x_data[0:64]
    train_x_data = train_x_data.values
    train_y_data = train_y_data.values

    test_x_data = data[64:]
    test_y_data = x_data[64:]
    test_x_data = test_x_data.values
    test_y_data = test_y_data.values

    model = keras.Sequential()

    model.add(keras.layers.Dense(10, activation=tf.nn.relu, input_shape=(train_x_data.shape[1],)))
    model.add(keras.layers.Dense(64, activation=tf.nn.relu))
    model.add(keras.layers.Dense(32, activation=tf.nn.relu))
    model.add(keras.layers.Dense(16, activation=tf.nn.relu))

    model.add(keras.layers.Dense(1, activation=tf.nn.sigmoid))

    model.summary()

    model.compile(optimizer='adam',
                  loss='binary_crossentropy',
                  metrics=['accuracy'])

    history = model.fit(train_x_data,
                        train_y_data,
                        epochs=800,
                        batch_size=256,
                        validation_data=(test_x_data, test_y_data),
                        verbose=1)

    loss, accuracy = model.evaluate(test_x_data, test_y_data)
    print("Accuracy", accuracy)
    print(model.predict(pd.DataFrame.from_dict({"ranking": [0.8], "surface": [0.35], "previous": [0.5]})))

    model.save("test_model.h5")
