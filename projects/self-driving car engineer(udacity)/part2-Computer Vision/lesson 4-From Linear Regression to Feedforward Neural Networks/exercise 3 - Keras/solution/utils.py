import logging

import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras.preprocessing import image_dataset_from_directory


def process(image,label):
    """ small function to normalize input images """
    image = tf.cast(image/255. ,tf.float32)
    return image,label


def display_metrics(history):
    """ plot loss and accuracy from keras history object """
    f, ax = plt.subplots(1, 2, figsize=(15, 5))
    ax[0].plot(history.history['loss'], linewidth=3)
    ax[0].plot(history.history['val_loss'], linewidth=3)
    ax[0].set_title('Loss', fontsize=16)
    ax[0].set_ylabel('Loss', fontsize=16)
    ax[0].set_xlabel('Epoch', fontsize=16)
    ax[0].legend(['train loss', 'val loss'], loc='upper right')
    ax[1].plot(history.history['accuracy'], linewidth=3)
    ax[1].plot(history.history['val_accuracy'], linewidth=3)
    ax[1].set_title('Accuracy', fontsize=16)
    ax[1].set_ylabel('Accuracy', fontsize=16)
    ax[1].set_xlabel('Epoch', fontsize=16)
    ax[1].legend(['train acc', 'val acc'], loc='upper left')
    plt.show()


def get_datasets(imdir):
    """ extract GTSRB dataset from directory """
    train_dataset = image_dataset_from_directory(imdir, 
                                       image_size=(32, 32),
                                       batch_size=256,
                                       validation_split=0.2,
                                       subset='training',
                                       seed=123,
                                       label_mode='int')
    val_dataset = image_dataset_from_directory(imdir, 
                                        image_size=(32, 32),
                                        batch_size=256,
                                        validation_split=0.2,
                                        subset='validation',
                                        seed=123,
                                        label_mode='int')
    train_dataset = train_dataset.map(process)
    val_dataset = val_dataset.map(process)
    return train_dataset, val_dataset


def get_module_logger(mod_name):
    logger = logging.getLogger(mod_name)
    handler = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s %(levelname)-8s %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)
    return logger
