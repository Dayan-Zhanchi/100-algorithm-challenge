import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import pairwise_distances_argmin
from sklearn.datasets.samples_generator import make_blobs


def k_means(training_data, k):
    prev_centers = forgy_initialization(training_data, k)
    while True:
        """ calculate the clusters and return a list of where each data point belong to which region
            because we use the pairwise module, we can just have the means in form of x and y points
            instead of explicitly calculating the means as a number """
        clusters = pairwise_distances_argmin(training_data, prev_centers)

        """ update step for the new centroids (new means)
            calculate the mean of each axis (i.e x and y) for each cluster
            the end result is a pair of (x,y), where x is the mean of all the x coords and ditto for y """
        curr_centers = np.asarray([training_data[clusters == i].mean(0)
                                   for i in range(k)])

        """ checks if all the values match along all dimensions of the array
            in this case we have e.g [[True,True], [False,True]] and True False will be
            compared as well as True True to see if they are the same
            we have true and false values because of the equality check in the np all == """
        if np.all(prev_centers == curr_centers):
            break

        prev_centers = curr_centers

    return prev_centers, clusters


# randomly sample k data points and make them the centers
def forgy_initialization(X, k):
    random_rows_to_select = np.random.choice(X.shape[0], k, replace=False)
    return X[random_rows_to_select]


def plot_clusters(centers, clusters, training_data):
    plt.scatter(training_data[:, 0], training_data[:, 1], c=clusters, s=50, cmap='viridis')
    plt.scatter(centers[:, 0], centers[:, 1], c='black', s=200, alpha=0.5);
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('K means clustering')
    plt.savefig('clusters.png')
    plt.show()


def generate_random_blobs(samples, c):
    X, y_true = make_blobs(n_samples=samples, centers=c,
                           cluster_std=0.90, random_state=0)
    plot_blobs(X)
    return X


def plot_blobs(X):
    plt.scatter(X[:, 0], X[:, 1], s=50)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Randomly generated blobs')
    plt.savefig('blobs.png')
    plt.show()
