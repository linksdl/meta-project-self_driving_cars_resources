import copy
import json
from collections import Counter

import matplotlib.pyplot as plt
import numpy as np

from utils import calculate_iou, check_results


if __name__ == '__main__':
    # load data
    with open('data/predictions.json', 'r') as f:
        preds = json.load(f)

    with open('data/ground_truths.json', 'r') as f:
        gts = json.load(f)

    # TODO IMPLEMENT THIS SCRIPT

    check_results(mAP)
