import io
import os
import argparse
import logging

import tensorflow.compat.v1 as tf
from PIL import Image
from waymo_open_dataset import dataset_pb2 as open_dataset

from utils import parse_frame, int64_feature, int64_list_feature, bytes_feature
from utils import bytes_list_feature, float_list_feature


def create_tf_example(filename, encoded_jpeg, annotations):
    """
    convert to tensorflow object detection API format
    args:
    - filename [str]: name of the image
    - encoded_jpeg [bytes-likes]: encoded image
    - annotations [list]: bboxes and classes
    returns:
    - tf_example [tf.Example]
    """
    # TO BE IMPLEMENTED  
    return tf_example


def process_tfr(path):
    """
    process a waymo tf record into a tf api tf record
    """
    # create processed data dir
    file_name = os.path.basename(path)

    logging.info(f'Processing {path}')
    writer = tf.python_io.TFRecordWriter(f'output/{file_name}')
    dataset = tf.data.TFRecordDataset(path, compression_type='')
    for idx, data in enumerate(dataset):
        frame = open_dataset.Frame()
        frame.ParseFromString(bytearray(data.numpy()))
        encoded_jpeg, annotations = parse_frame(frame)
        filename = file_name.replace('.tfrecord', f'_{idx}.tfrecord')
        tf_example = create_tf_example(filename, encoded_jpeg, annotations)
        writer.write(tf_example.SerializeToString())
    writer.close()


if __name__ == "__main__": 
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--path', required=True, type=str,
                        help='Waymo Open dataset tf record')
    args = parser.parse_args()  
    process_tfr(args.path)