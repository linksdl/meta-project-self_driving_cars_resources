# Exercise 1 - Pooling

## Objective

In this exercise, you will implement a simplified version of the max pooling layer.

## Details

You will have to implement two functions and a small script. The first function is a padding 
function. Using the input size and the pooling layer parameters (stride and filter size), 
this function finds the padding `wpad` and `hpad` (width and height padding) such that the 
input dimensions are padded.

The next function calculates the output dimensions after pooling given the padded array
dimensions and the pooling parameters (stride and filter size).

Finally, the script calculates the pooling layer output.

You can run `python pooling.py` to check your implementation - note that the checking of the output will require input of a 3x3 filter and stride of 3.

## Tips

Pooling only affects the spatial dimensions and preserves the batch size (first axis of the padded array) 
and the number of channels (last axis).
