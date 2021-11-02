import json

import numpy as np


def check_results(ious):
    # check the results
    solution = np.load('../data/exercise1_check.npy')
    assert (ious == solution).sum() == 40, 'The iou calculation is wrong!'
    print('Congrats, the iou calculation is correct!')
    

def get_data():
    """ simple wrapper function to get data """
    with open('../data/ground_truth.json') as f:
        ground_truth = json.load(f)
    
    with open('../data/predictions.json') as f:
        predictions = json.load(f)

    return ground_truth, predictions