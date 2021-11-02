import json


def get_data():
    """ simple wrapper function to get data """
    with open('data/ground_truth.json') as f:
        ground_truth = json.load(f)
    
    with open('data/predictions.json') as f:
        predictions = json.load(f)

    return ground_truth, predictions