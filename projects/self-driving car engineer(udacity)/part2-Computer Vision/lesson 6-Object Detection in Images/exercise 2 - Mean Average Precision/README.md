# Exercise 2 - Mean Average Precision

## Objective

In this exercise, you will have to implement the Mean Average Precision (mAP) metric.

## Details

To do so, you will first have to create the Precision-Recall (PR) curve. Once this curve is created, you 
need to create the smoothed version as discussed in the lesson. Finally you can use this smoothed
version to calculate the mAP.

You also have to create a visualization of the PR and smoothed PR curves.

Make sure to check the `Desktop` to see your visualization when running the code.

## Tips

To create the PR curve, you need to sort the predictions based on their confidence score and calculate the precision and recall for each subset of the predictions, as explained in the course.

To make your life easier, you can hard code the smoothed PR curve based on the PR curve, but 
you should think of a scripted version of doing so.
