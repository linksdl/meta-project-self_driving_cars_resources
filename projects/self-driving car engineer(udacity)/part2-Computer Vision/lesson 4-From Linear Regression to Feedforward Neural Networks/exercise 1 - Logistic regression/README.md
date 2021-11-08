# Exercise 1 - Logistic regression

## Objective

In this exercise, you have to implement 4 different functions:
* `softmax`: compute the softmax of a vector. This function takes as input a tensor and outputs a discrete probability distribution. 

* `cross_entropy`: calculate the cross entropy loss given a vector of predictions (after softmax) and a vector of ground truth (one-hot vector).

* `model`: takes a batch of images (stack of images along the first dimensions) and feeds it through the logistic regression model

* `accuracy`: given a vector of predictions and a vector of ground truth, calculates the accuracy.

As always, you can run `python logistic.py` to check your implementation.

## Tips

You can leverage the `tf.boolean_mask` function to calculate the cross entropy. Keep in mind
that most elements of the ground truth vector are zeros.