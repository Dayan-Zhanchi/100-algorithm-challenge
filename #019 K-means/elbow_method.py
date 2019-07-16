import k_means
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import pairwise_distances


def elbow_method(data):
    sum_of_squared_distances = []
    for k in range(1, 15):
        centers, clusters = k_means.k_means(data, k)
        ssd = 0
        for i in range(k):
            ssd += np.sum(pairwise_distances(data[clusters == i], [centers[i]]))
        sum_of_squared_distances.append(ssd)

    return sum_of_squared_distances


def plot_elbow(ssd):
    k = [i for i in range(1, 15)]
    plt.plot(k, ssd, 'bx-')
    plt.xlabel('k')
    plt.ylabel('sum of squared distances')
    plt.title('Elbow method for sum of squared distances')
    plt.savefig('elbow.png')
    plt.show()
