import numpy as np 


def check_results(mean, std):
    # calculate L1 distance
    gt_mean = np.array([ 95.30968145, 110.46818685, 123.70005162])
    mean_dst = np.sum(np.abs(np.array(mean) - gt_mean))
    assert mean_dst < 0.0001, 'The mean calculation is incorrect.'

    gt_std = np.array([47.02613582, 52.31789603, 59.47874234])
    std_dst = np.sum(np.abs(np.array(std) - gt_std))
    assert std_dst < 0.0001, 'The std calculation is incorrect.'
    print('Congrats, all calculations are correct!')