# Exercise 3 - Create tf records

## Objective
The goal of this exercise is to make you familiar with the tf record format. In particular, 
your job is to convert the data from the Waymo Open Dataset into a new tf record format that we 
will use for the final project, as there is a difference between the format used for the 
Waymo Open Dataset and that used by the TensorFlow Object Detection API.

## Details

You can read more about the Waymo Open Dataset data format [here](https://waymo.com/open/data/perception/). 
Each tf record files contains the data for an entire trip made by the car, meaning that 
it contains images from the different cameras as well as LIDAR data. Because we want 
to keep our dataset small, we are implementing the `create_tf_example` function to 
create cleaned tf records files.

We are using the Waymo Open Dataset github repository to parse the raw tf record files. 
would recommend to follow [this tutorial](https://github.com/waymo-research/waymo-open-dataset) 
to better understand the data format before diving into this exercise. 

## Tips

This [document](https://github.com/Jossome/Waymo-open-dataset-document) provides
an overview of the dataset structure.

Later on, we will leverage the Tensorflow Object Detection API to train Object Detection models.
In the API tutorial, you can find an example of `create_tf_example` [here](https://tensorflow-object-detection-api-tutorial.readthedocs.io/en/latest/training.html#create-tensorflow-records).

Note that running the code will require the use of the example `.tfrecord` included in the `/home/workspace` directory. You will need the GPU enabled (see bottom left of workspace) for the appropriate libraries to be available in the workspace as well.