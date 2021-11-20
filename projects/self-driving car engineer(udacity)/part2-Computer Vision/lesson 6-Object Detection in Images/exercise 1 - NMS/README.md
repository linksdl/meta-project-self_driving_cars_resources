# Exercise 1 - NMS

## Objective

In this exercise, you have to implement the Non-Max Suppression algorithm.

## Details

You are given a json file containing a list of predictions, containing `boxes` and `scores`.
You will leverage the `calculate_iou` function to calculate the Intersection Over Union of 
these different predictions and implement the NMS algorithm.

To do so, you will need to:
* compare each bounding box with all the other bounding boxes in the set
* for each pair of bounding boxes, calculate the IoU and compare the scores
* if the IoU is above the threshold, keep the box with the highest score

You can run `python nms.py` to check your implementation.

## Tips

You should also think of the modifications to make to implement Soft NMS.
