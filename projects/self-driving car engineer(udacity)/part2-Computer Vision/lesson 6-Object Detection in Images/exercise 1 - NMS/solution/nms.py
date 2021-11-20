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

    data = []
    for bb, sc in zip(predictions['boxes'], predictions['scores']):
        data.append([bb, sc])

    data_sorted = sorted(data, key = lambda k: k[1])[::-1]
    filtered = []
    for i, bi in enumerate(data_sorted):
        discard = False
        for j, bj in enumerate(data_sorted):
            if i == j:
                continue
            iou = calculate_iou(bi[0], bj[0])
            if iou > 0.5:
                if bj[1] > bi[1]:
                    discard = True
        if not discard:
            filtered.append(bi)
    return filtered


if __name__ == '__main__':
    with open('../data/predictions_nms.json', 'r') as f:
        predictions = json.load(f)

    filtered = nms(predictions)
    check_results(filtered)
