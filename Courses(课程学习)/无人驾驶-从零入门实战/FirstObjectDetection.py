# -*- coding:utf-8 -*-
"""
@author:ZJX
@file:FirstObjectDetection.py
@time:2018/7/311:13
"""
# To use ImageAI in your application developments, you must have installed the following dependencies before you install ImageAI :
#
#
# - Python 3.5.1 (and later versions) Download (Support for Python 2.7 coming soon)
# - pip3 Install
# - Tensorflow 1.4.0 (and later versions) Install or install via pip
#  pip3 install --upgrade tensorflow
#
# - Numpy 1.13.1 (and later versions) Install or install via pip
#  pip3 install numpy
# - SciPy 0.19.1 (and later versions) Install or install via pip
#  pip3 install scipy
# - OpenCV Install or install via pip
#  pip3 install opencv-python
# - Pillow Install or install via pip
#  pip3 install pillow
# - Matplotlib Install or install via pip
#  pip3 install matplotlib
# - h5py Install or install via pip
#  pip3 install h5py
# - Keras 2.x Install or install via pip
#  pip3 install keras
# Installation
# To install ImageAI, run the python installation instruction below in the command line:
#
# pip3 install https://github.com/OlafenwaMoses/ImageAI/releases/download/2.0.1/imageai-2.0.1-py3-none-any.whl
#
#
# or download the Python Wheel imageai-2.0.1-py3-none-any.whl and run the python installation instruction in the command line to the path of the file like the one below:
#
# pip3 install C:\User\MyUser\Downloads\imageai-2.0.1-py3-none-any.whl
#
# 下载用于目标检测的RetinaNet模型文件: https://github.com/OlafenwaMoses/ImageAI/releases/download/1.0/resnet50_coco_best_v2.0.1.h5



from imageai.Detection import ObjectDetection
import os

execution_path = os.getcwd()

detector = ObjectDetection()
detector.setModelTypeAsRetinaNet()
detector.setModelPath(os.path.join(execution_path,"resnet50_coco_best_v2.0.1.h5" ))
detector.loadModel()
detections = detector.detectObjectsFromImage(input_image=os.path.join(execution_path,"image2.jpg"),output_image_path=os.path.join(execution_path,"image2new.jpg"))

for eachObject in detections:
    print(eachObject["name"]+" : " + eachObject["percentage_probability"])
    print("-----------------------------------")

# detections, objects_path = detector.detectObjectsFromImage(input_image=os.path.join(execution_path , "image3.jpg"), output_image_path=os.path.join(execution_path , "image3new.jpg"), extract_detected_objects=True)
#
# for eachObject, eachObjectPath in zip(detections, objects_path):
#     print(eachObject["name"] + " : " + eachObject["percentage_probability"] )
#     print("Object's image saved in " + eachObjectPath)
#     print("--------------------------------")
