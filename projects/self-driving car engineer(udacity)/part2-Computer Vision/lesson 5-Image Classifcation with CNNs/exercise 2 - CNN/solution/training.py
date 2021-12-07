import argparse
import logging

import tensorflow as tf
from tensorflow.keras.layers import Dense, Flatten, Conv2D, MaxPooling2D

from utils import get_datasets, get_module_logger, display_metrics


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


if __name__  == '__main__':
    logger = get_module_logger(__name__)
    parser = argparse.ArgumentParser(description='Download and process tf files')
    parser.add_argument('-d', '--imdir', required=True, type=str,
                        help='data directory')
    parser.add_argument('-e', '--epochs', default=10, type=int,
                        help='Number of epochs')
    args = parser.parse_args()

    logger.info(f'Training for {args.epochs} epochs using {args.imdir} data')
    # get the datasets
    train_dataset, val_dataset = get_datasets(args.imdir)

    model = create_network()

    model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])
    history = model.fit(x=train_dataset,
                        epochs=args.epochs,
                        validation_data=val_dataset)
    display_metrics(history)
