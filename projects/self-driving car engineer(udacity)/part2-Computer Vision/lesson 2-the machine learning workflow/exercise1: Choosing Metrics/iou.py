import numpy as np

from utils import get_data, check_results


def calculate_iou(gt_bbox, pred_bbox):
    """
    calculate iou
    args:
    - gt_bbox [array]: 1x4 single gt bbox
    - pred_bbox [array]: 1x4 single pred bbox
    returns:
    - iou [float]: iou between 2 bboxes
    """
    ## IMPLEMENT THIS FUNCTION
    # x_inter1 = max(gt_bbox[0], pred_bbox[0])
    # y_inter1 = max(gt_bbox[1], pred_bbox[1])
    #
    # x_inter2 = min(gt_bbox[2], pred_bbox[2])
    # y_inter2 = min(gt_bbox[3], pred_bbox[3])

    x1, y1, x2, y2 = gt_bbox
    x3, y3, x4, y4 = pred_bbox
    x_inter1 = max(x1, x3)
    y_inter1 = max(y1, y3)
    x_inter2 = min(x2, x4)
    y_inter2 = min(y2, y4)

    # compute the area of intersection rectangle
    interArea = max(0, x_inter2 - x_inter1) * max(0, y_inter2 - y_inter1)
    # compute the area of both the prediction and ground-truth
	# rectangles

    # gt_area = (gt_bbox[2] - gt_bbox[0]) * (gt_bbox[3] - gt_bbox[1])
    # pred_area = (pred_bbox[2] - pred_bbox[0]) * (pred_bbox[3] - pred_bbox[1])

    boxAArea = (x2 - x1) * (y2 - y1)
    boxBArea = (x4 - x3) * (y4 - y3)
    # compute the intersection over union by taking the intersection
	# area and dividing it by the sum of prediction + ground-truth
	# areas - the interesection area
    iou = interArea / float(boxAArea + boxBArea - interArea)
    # iou = interArea / float(gt_area + pred_area - interArea)
    # return the intersection over union value
    return iou

def calculate_ious(gt_bboxes, pred_bboxes):
    """
    calculate ious between 2 sets of bboxes
    args:
    - gt_bboxes [array]: Nx4 ground truth array
    - pred_bboxes [array]: Mx4 pred array
    returns:
    - iou [array]: NxM array of ious
    """
    ious = np.zeros((gt_bboxes.shape[0], pred_bboxes.shape[0]))
    for i, gt_bbox in enumerate(gt_bboxes):
        for j, pred_bbox in enumerate(pred_bboxes):
            ious[i,j] = calculate_iou(gt_bbox, pred_bbox)
    return ious

if __name__ == "__main__":
    ground_truth, predictions = get_data()
    # for e in ground_truth:
    #     print(e)
    # get bboxes array
    filename = 'segment-1231623110026745648_480_000_500_000_with_camera_labels_38.png'
    gt_bboxes = [g['boxes'] for g in ground_truth if g['filename'] == filename][0]
    gt_bboxes = np.array(gt_bboxes)
    pred_bboxes = [p['boxes'] for p in predictions if p['filename'] == filename][0]
    pred_boxes = np.array(pred_bboxes)

    ious = calculate_ious(gt_bboxes, pred_boxes)
    # print(ious)
    check_results(ious)
