import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Rectangle
from PIL import Image


def display_results(img, bboxes, aug_img, aug_bboxes):
    f, ax = plt.subplots(1, 2, figsize=(10, 10))
    ax[0].imshow(img)
    for bb in bboxes:
        y1, x1, y2, x2 = bb
        rec = Rectangle((x1, y1), x2-x1, y2-y1, facecolor='none', edgecolor='r')
        ax[0].add_patch(rec)
    
    ax[1].imshow(aug_img)
    for bb in aug_bboxes:
        y1, x1, y2, x2 = bb
        rec = Rectangle((x1, y1), x2-x1, y2-y1, facecolor='none', edgecolor='r')
        ax[1].add_patch(rec)
    plt.show()


def check_results(img, boxes, aug_type, classes=None):
    if aug_type == 'hflip':
        imcheck = Image.open('../data/augmented/flipped.png')
        bbcheck = np.load('../data/augmented/flipped.npy')
        assert np.array_equal(np.array(imcheck), np.array(img)), 'Horizontal flip is wrong!'
        assert np.array_equal(np.array(boxes), bbcheck), 'Horizontal flip is wrong!'
        print('Horizontal flip is working')

    elif aug_type == 'resize':
        imcheck = Image.open('../data/augmented/resized.png')
        bbcheck = np.load('../data/augmented/resized.npy')
        assert np.array_equal(np.array(imcheck), np.array(img)), 'Resizing is wrong!'
        assert np.array_equal(np.array(boxes), bbcheck), 'Resizing is wrong!'
        print('Resizing is working')

    elif aug_type == 'random_crop':
        imcheck = Image.open('../data/augmented/cropped.png')
        bbcheck = np.load('../data/augmented/cropped_bb.npy')
        clcheck = np.load('../data/augmented/cropped_cl.npy')
        assert np.array_equal(np.array(imcheck), np.array(img)), 'Cropping is wrong!'
        assert np.array_equal(np.array(boxes), bbcheck), 'Cropping is wrong!'
        assert np.array_equal(np.array(classes), clcheck), 'Cropping is wrong!'
        print('Cropping is working')
    return