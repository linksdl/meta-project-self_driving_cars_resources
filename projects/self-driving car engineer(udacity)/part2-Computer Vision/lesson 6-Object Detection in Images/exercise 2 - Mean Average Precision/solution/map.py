import copy
import json
from collections import Counter

import matplotlib.pyplot as plt
import numpy as np

from utils import calculate_iou, check_results


if __name__ == '__main__':
    # load data
    with open('../data/predictions.json', 'r') as f:
        preds = json.load(f)

    with open('../data/ground_truths.json', 'r') as f:
        gts = json.load(f)

    # sort predictions by scores
    boxes = preds[0]['boxes']
    classes = preds[0]['classes']
    scores = preds[0]['scores']

    predictions = [(bb, cl, sc) for bb, cl,sc in zip(boxes, classes, scores)]
    predictions = sorted(predictions, key=lambda k:k[-1])[::-1]

    # create precision - recall plot
    total = len(gts[0]['boxes'])
    tp = 0
    curve = []
    for idx, pred in enumerate(predictions):
        for bb in gts[0]['boxes']:
            iou = calculate_iou(bb, pred[0])
            # print(iou)
            if iou > 0.5:
                if pred[1] == 1:
                    tp += 1
        prec = tp / (idx+1)
        rec = tp / total
        curve.append([prec, rec])

    # smooth PR curve
    curve = np.array(curve)
    ct = Counter(curve[:, 1])
    boundaries = sorted([k for k,v in ct.items() if v > 1])
    # get max precision values
    maxes = []
    for i in range(len(boundaries)):
        if i != len(boundaries) - 1:
            loc = [p[0] for p in curve if boundaries[i+1] >= p[1] > boundaries[i]]
            maxes.append(np.max(loc))
        else:
            loc = [p[0] for p in curve if p[1] > boundaries[i]]
            maxes.append(np.max(loc))
    smoothed = copy.copy(curve)
    replace = -1
    for i in range(smoothed.shape[0]-1):
        if replace != -1:
            smoothed[i, 0] = maxes[replace]
        if smoothed[i, 1] == smoothed[i+1, 1]:
            replace += 1

    plt.plot(curve[:, 1], curve[:, 0], linewidth=4)
    plt.plot(smoothed[:, 1], smoothed[:, 0], linewidth=4)
    plt.xlabel('recall', fontsize=18)
    plt.ylabel('precision', fontsize=18)
    plt.show()

    # calculate mAP
    cmin = 0
    mAP = 0
    for i in range(smoothed.shape[0] - 1):
        if smoothed[i, 1] == smoothed[i+1, 1]:
            mAP += (smoothed[i, 1] - cmin) * smoothed[i, 0]
            cmin = smoothed[i, 1]
    mAP += (smoothed[-1, 1] - cmin) * smoothed[-1, 0]
    check_results(mAP)
