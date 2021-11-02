# Exercise 2 - Visualization

## Objective

For this exercise, you need to implement a function to visualize the ground truth boxes
on a set of images in `visualization.py`. You need to display color coded bounding boxes using the class id associated
with each bounding box. You need to display all the data in a single figure.
You should aim for visibility as clear data visualization is critical to communicate a message.

![](example.png)

**Note:** Any visualized code will only pop up through the workspace desktop - if you complete work in the primary workspace window, you'll need to click the "Desktop" button in the bottom right to view visualizations.

## Details

The data is located is the `ground_truth.json` file. It contains 20 observations, each observation is a dict
with the following fields.

```
{filename: str, boxes: [list[list]], classes: list}
```
The bounding boxes are using the `[x1, y1, x2, y2]` format.

## Tips
You can use matplotlib patches to create the bounding boxes visualizations. You can improve over the above visualization by adding the classes name by the bounding boxes.