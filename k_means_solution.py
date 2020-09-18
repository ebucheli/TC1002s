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
    return np.sqrt(np.sum((np.array(b)-np.array(a))**2))

def get_clusters(points,centroids):
    """
    Returns a list of clusters given all the points in the dataset and
    the current centroids.
    Input:
        points (list of lists): A list with every point in the dataset
        centroids (list of lists): A list with the current centroids
    Output:
        clusters (list of lists of lists): A List of Clusters. Each cluster
        is also a list of points in the cluster.
    """
    clusters = [[] for f in centroids]

    for i, point in enumerate(points):
        point_to_centroids = []
        for j, centroid in enumerate(centroids):
            point_to_centroids.append(distance(point,centroid))
        closest_idx = np.argmin(point_to_centroids)
        clusters[closest_idx].append(point)

    return clusters

def update_centroids(clusters):
    """
    Given a list of clusters (as prepared by get_clusters) get the new centroids
    Input:
        clusters (list of lists of lists): A List of Clusters. Each cluster
        is also a list of points in the cluster.
    Output:
        A (list of lists): The new centroids.
    """
    new_centroids = []

    for cluster in clusters:
        new_centroids.append(np.mean(cluster,axis = 0))
    return new_centroids



def k_means(points, k, iterations=10):
    """
    K Means Unsupervised ML Algorithm Implementation with Forgy Initialization
    Input:
        points (numpy array): a 2D Array with the data to cluster.
        k (int): The number of clusters to find
    """
    idx = np.random.randint(len(points),size=k)

    centroids = points[idx,:]
    clusters = get_clusters(points,centroids)

    for i in range(iterations):

        if i % 1 == 0:
            if i == 0:
                title = "Initialization"
            else:
                title = "Iteration {}".format(i+1)

            show_clusters_centroids(
                clusters,
                centroids,
                title,
            )

        clusters = get_clusters(points,centroids)
        centroids = update_centroids(clusters)

    return clusters,centroids


if __name__ == "__main__":
    data = load_data('./data/iris.data')
    k = 3

    X = np.array([f[:-1] for f in data])
    y = np.array([f[-1] for f in data])

    clusters,centroids = k_means(X,3)

    show_clusters_centroids(clusters,centroids,"Result", keep=True)
    plt.show()
