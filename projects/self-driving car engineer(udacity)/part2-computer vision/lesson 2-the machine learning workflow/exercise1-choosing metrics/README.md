# Exercise 1 

## Part 1 - Calculate IoU

### Objectives

In the first part of this exercise, your task is to implement a function that calculates the iou between
two bounding boxes. 

### Details

The `calculate_ious` function in `iou.py` takes two arrays containing the bounding boxes coordinates
as inputs. Both arrays are 1x4 numpy arrays. The array are using the following format:
```
[x1, y1, x2, y2]
```
where `x1 < x2` and `y1 < y2`. `(x1, y1)` are the coordinates of the upper left corner 
and `(x2, y2)` the coordinates of the lower right corner of the bounding box.

### Example

```
iou = calculate_iou(np.array([0, 0, 100, 100]), np.array([101, 101, 200, 200]))
```

### Tips

Keep in mind that the bounding boxes may not intersect, in which case the IoU 
should be equal to 0.

By running `python iou.py`, you will be able to check your implementation. 


## Part 2 - calculate Precision / Recall

### Objectives

Then, you are asked to calculate the precision and recall for a given set of predictions 
and ground truths. You will use a threshold of 0.5 IoU to determine if a prediction is 
a true positive or not.

### Details

The `precision_recall` function in `precision_recall.py` takes as inputs a `ious` NxM array of IoU values as well as 
two list `pred_classes` and`gt_classes` containing the M predicted classes ids and the N ground truth classes ids.

The `ious` array contains the pairwise IoU values between the N ground truth bounding boxes and the M 
predicted bounding boxes such that:

```
ious[x, y] = calculate_iou(groundtruth[x], predictions[y])
```

### Example

```
precision, recall = precision_recall(np.array([[0.5, 0.1], [0.8, 0.1]), np.array([1, 2]), np.array([1, 0]))
```

### Tips

You need to calculate the number of False Negatives to calculate the recall. You can use the IoU array
to find the ground truth bounding boxes that are not predicted.

By running `python precision_recall.py`, you will be able to check your implementation.
