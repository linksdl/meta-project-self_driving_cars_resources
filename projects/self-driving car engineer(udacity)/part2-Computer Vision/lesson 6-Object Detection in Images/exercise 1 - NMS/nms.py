import json

from utils import calculate_iou, check_results


def nms(predictions):
    """
    non max suppression
    args:
    - predictions [dict]: predictions dict
    returns:
    - filtered [list]: filtered bboxes and scores
    """
    filtered = []
    # IMPLEMENT THIS FUNCTION
    return filtered


if __name__ == '__main__':
    with open('data/predictions_nms.json', 'r') as f:
        predictions = json.load(f)

    filtered = nms(predictions)
    check_results(filtered)
