import pandas as pd
import matplotlib.pyplot as plt
from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn.dummy import DummyClassifier
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import Normalizer
import tensorflow as tf
from keras.applications import VGG16
from keras.layers import Dense, Flatten
from keras.optimizers import Adam
from keras import Model


def baseline_model(X_train, y_train, X_test, y_test):
    dummy = DummyClassifier(strategy='most_frequent')
    dummy.fit(X_train, y_train)
    return dummy.score(X_test, y_test)


def svm_classifier(X_train, y_train, X_test, y_test, kernel, num_samples=5000):
    pipe = Pipeline([('normalizer', Normalizer()),
                    ('svc', svm.SVC(kernel=kernel))])
    pipe.fit(X_train[:num_samples], y_train[:num_samples])
    return pipe.score(X_test, y_test)


def create_cnn(num_classes):
    base = VGG16(include_top=False,
                 input_shape=(64, 64, 3),
                 weights='imagenet')

    _x = base.output
    _x = Flatten()(_x)
    _x = Dense(512, activation='relu')(_x)
    _x = Dense(64, activation='relu')(_x)
    predictions = Dense(num_classes, activation='softmax')(_x)
    cnn = Model(inputs=base.input, outputs=predictions)

    for layer in cnn.layers[:5]:
        layer.trainable = False

    cnn.compile(optimizer=Adam(0.0001),
                loss='sparse_categorical_crossentropy',
                metrics=['accuracy'])

    return cnn
