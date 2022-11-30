# Q3_graded

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.layers import Input, Dense, Flatten
from tensorflow.keras.optimizers import SGD
from tensorflow.keras.models import Model
from tensorflow.keras.callbacks import EarlyStopping, ReduceLROnPlateau
from tensorflow.keras import datasets
from tensorflow.keras.utils import to_categorical
import matplotlib.pyplot as plt
import numpy as np


def create_train_model(x_train, y_train, x_test, y_test, layer_num, weight_decay, momentum):
    inputs = Input(shape=x_train[0].shape)
    h = Flatten()(inputs)

    for i in range(layer_num):
        h = Dense(256, activation="relu")(h)
    outputs = Dense(10, activation="softmax")(h)

    model = Model(inputs=inputs,outputs=outputs)

    early_stopping=EarlyStopping(monitor='val_accuracy',patience=5,min_delta=0.01,mode='max')
    # learning_rate_reduction=ReduceLROnPlateau(patience=5,factor=0.2,min_lr=0.0001)

    if momentum and weight_decay:
        model.compile(optimizer=SGD(learning_rate=0.01, momentum=0.9, decay = 0.01 / 50),
                  loss='categorical_crossentropy',
                  metrics=['accuracy']
                  )
    elif momentum:
        model.compile(optimizer=SGD(learning_rate=0.01, momentum=0.9),
                  loss='categorical_crossentropy',
                  metrics=['accuracy']
                  )
    elif weight_decay:
        model.compile(optimizer=SGD(learning_rate=0.01, decay = 0.01 / 50),
                  loss='categorical_crossentropy',
                  metrics=['accuracy']
                  )
    else:
        model.compile(optimizer=SGD(learning_rate=0.01),
                  loss='categorical_crossentropy',
                  metrics=['accuracy']
                  )

    history = model.fit(x_train, y_train, batch_size=256, epochs=200, verbose=2, validation_split=0.1, callbacks=[early_stopping])

    print(f"layer_num = {layer_num}, weight_decay = {weight_decay}, momentum = {momentum}")
    # fig, ax = plt.subplots()
    # ax.plot(history.history["val_accuracy"], label='val_acc')
    # ax.plot(history.history["val_loss"],label='val_loss')
    # leg = ax.legend();
    plt.plot(history.history["val_accuracy"])
    plt.show()
    # ax.title(f"layer_num = {layer_num}")
    print("=========================================")


# Q3_graded
# Do not change the above line.


(x_train, y_train), (x_test, y_test) = datasets.cifar10.load_data()

x_train, x_test = x_train / 255, x_test / 255

y_train = to_categorical(y_train, num_classes=10)
y_test = to_categorical(y_test, num_classes=10)

layers = [2, 3]

for layer_num in layers:
    for momentum in [True, False]:
        for weight_decay in [True, False]:
            create_train_model(x_train, y_train, x_test, y_test, layer_num, weight_decay, momentum)

# Type your code here

