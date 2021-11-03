import matplotlib.pyplot as plt


def plot_histogram(img):
    """ plot channel-wise pixel value distribution """
    histogram = img.histogram()

    R = histogram[0:256]
    G = histogram[256:512]
    B = histogram[512:768]

    plt.plot(range(256), R, color='r')
    plt.fill_between(range(256), R, color='r', alpha=0.5)
    plt.plot(range(256), G, color='g')
    plt.fill_between(range(256), G, color='g', alpha=0.5)
    plt.plot(range(256), B, color='b')
    plt.fill_between(range(256), B, color='b', alpha=0.5)
    plt.show()
