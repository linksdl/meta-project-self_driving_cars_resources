import logging

import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import tensorflow as tf
from tensorflow.keras.layers import Dense, Flatten, Conv2D, MaxPooling2D
from tensorflow.keras.preprocessing import image_dataset_from_directory


class LrLogger(tf.keras.callbacks.Callback):
    def __init__(self):
        super().__init__()

    def on_train_begin(self, logs=None):
        history = self.model.history.history
        history['lr'] = []

    def on_epoch_end(self, epoch, logs=None):
        history = self.model.history.history
        optimizer = self.model.optimizer
        decayed_lr = optimizer._decayed_lr('float32').numpy()
        history['lr'].append(decayed_lr)


def process(image,label):
    """ small function to normalize input images """
    image = tf.cast(image/255. ,tf.float32)
    return image,label


def create_network():
    net = tf.keras.models.Sequential()
    input_shape = [32, 32, 3]
    net.add(Conv2D(6, kernel_size=(3, 3), strides=(1, 1), activation='relu',
                   input_shape=input_shape))
    net.add(MaxPooling2D(pool_size=(2, 2), strides=(2, 2)))
    net.add(Conv2D(16, kernel_size=(3, 3), strides=(1, 1), activation='relu'))
    net.add(MaxPooling2D(pool_size=(2, 2), strides=(2, 2)))
    net.add(Flatten())
    net.add(Dense(120, activation='relu'))
    net.add(Dense(84, activation='relu'))
    net.add(Dense(43))
    return net


def display_metrics(history):
    """ plot loss and accuracy from keras history object """
    f, ax = plt.subplots(1, 3, figsize=(15, 5))
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
    ax[2].plot(history.history['lr'], linewidth=3)
    ax[2].set_title('Learning rate', fontsize=16)
    ax[2].set_ylabel('Learning Rate', fontsize=16)
    ax[2].set_xlabel('Epoch', fontsize=16)
    ax[2].legend(['learning rate'], loc='upper right')
    # ax[2].ticklabel_format(axis='y', style='sci')
    ax[2].yaxis.set_major_formatter(mtick.FormatStrFormatter('%.2e'))
    plt.tight_layout()
    plt.show()


def get_datasets(imdir):
    """ extract GTSRB dataset from directory """
    train_dataset = image_dataset_from_directory(imdir,
                                       image_size=(32, 32),
                                       batch_size=32,
                                       validation_split=0.2,
                                       subset='training',
                                       seed=123,
                                       label_mode='int')

    val_dataset = image_dataset_from_directory(imdir,
                                        image_size=(32, 32),
                                        batch_size=32,
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
