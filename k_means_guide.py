import numpy as np
import random
import matplotlib.pyplot as plt
import matplotlib

from io_utilities import load_data
from visualizations import show_clusters_centroids

def distance(a,b):
    """
    Compute Euclidean Distance Between Two Points
    Input:
        a (list): an n-dimensional list or array
        b (list): an n-dimensional list or array
    Output:
        The Euclidean Distance between vectors a and b
    """

    # All you need to do here is calculate the Euclidean Distance between
    # points a and b and return it

    euc_dist = # You code here!

    return euc_dist

def get_clusters(points,centroids):
    """
    Returns a list of clusters given all the points in the dataset and
    the current centroids.
    Input:
        points (numpy array): a 2D (M,N) Array with the data to cluster.
        M = Instances, N = Variables.
        centroids (list of numpy arrays): A list with the k current centroids
    Output:
        clusters (list of lists of numpy arrays): A List of Clusters. Each cluster
        is also a list of numpy arrays.
    """
    clusters = [[] for f in centroids]

    for i, point in enumerate(points):
        point_to_centroids = []
        for j, centroid in enumerate(centroids):
            # Make sure you find the distance from each point to the
            # centroid and append it to point_to_centroids
        # Now find the index of the smallest value in point_to_centroids
        # and use it to add the point to the corresponding cluster

    return clusters

def update_centroids(clusters):
    """
    Given a list of clusters (as prepared by get_clusters()) get the new centroids
    Input:
        clusters (list of numpy arrays): A List of Clusters. Each cluster
        is a 2D Array, rows = instances, columns=variables
    Output:
        A (list of numpy arrays): The new centroids.
    """
    new_centroids = []

    for cluster in clusters:
        # Find the average for each row in the cluster.
        # TIP: use the power of numpy!

        centroid = # You Code here
        new_centroids.append(centroid)

    return new_centroids



def k_means(points, k, iterations=10):
    """
    K Means Unsupervised ML Algorithm Implementation with Forgy Initialization
    Input:
        points (numpy array): a 2D (M,N) Array with the data to cluster.
        M = Instances, N = variables.
        k (int): The number of clusters to find
    """
    idx = np.random.randint(len(points),size=k)

    centroids = points[idx,:]
    clusters = get_clusters(points,centroids)

    for i in range(iterations):

        # Use get_clusters() and update_centroids() for each iteration.

    return clusters,centroids


if __name__ == "__main__":
    data = load_data('./data/iris.data')
    k = 3

    X = np.array([f[:-1] for f in data])
    y = np.array([f[-1] for f in data])

    clusters,centroids = k_means(X,3)

    show_clusters_centroids(clusters, centroids, "Result", keep=True)
