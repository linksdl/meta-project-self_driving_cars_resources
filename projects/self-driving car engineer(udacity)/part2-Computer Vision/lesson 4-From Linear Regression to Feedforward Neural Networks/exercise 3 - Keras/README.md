# Exercise 3 - Keras

## Objective

In this exercise, you will learn how to leverage the [Keras API](https://www.tensorflow.org/api_docs/python/tf/keras)
to create a small neural network. 

## Details

Keras was initially created as an independent API, providing easy ways to create and train neural networks using the same
interface but different backend libraries (such as Tensorflow). Whereas Tensorflow is a low-level library,
Keras codebase make it beginner friendly. 

The neural network you create should have less than 4 layers, including the output layer. This last layer should not be activated. Take the time to experiment with different architecture (number of layers, number of neurons) and see how it impacts the results.

You will need to specify the `--imdir`, e.g. `--imdir GTSRB/Final_Training/Images/`, using the provided GTSRB dataset.

Lastly, at the end of training, you will need to be in the `Desktop` view to see the metrics visualization.

## Tips

You can leverage `tf.keras.Sequential` to stack layers in your network and `tf.keras.layers` to create the different layers.
