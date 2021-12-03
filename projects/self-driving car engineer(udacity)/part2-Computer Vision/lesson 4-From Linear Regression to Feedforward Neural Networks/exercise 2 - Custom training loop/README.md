# Exercise 2 - Custom training loop

## Objective

In this exercise, you have to implement your first training and validation loops from scratch to train
the logistic model you implemented. To do so, you will also have to create an optimizer.

## Details

A training loop goes through element of the training dataset and uses it to update the model's weights.
A validation loop goes through each element of the validation dataset and uses it to calculate
the metrics (eg, accuracy). We call **epoch** an iteration of one training loop and one validation loop.

The input to your model should be normalized. You can do this by dividing them by 255: `X /= 255`.

You can run `python training.py` to train your first machine learning model!

You will need to specify the `--imdir`, e.g. `--imdir GTSRB/Final_Training/Images/`, using the provided GTSRB dataset.

## Tips

You don't need `tf.GradientTape` for the validation loop as you will not be updating gradients. 

The `assign_sub` Variable method will be useful to perform the weights update in the sgd optimizer.

Use the `tf.one_hot` function to get the one vector from the ground truth label.
