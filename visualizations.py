import numpy as np
import matplotlib.pyplot as plt
import os

COLORS = [
    'tab:blue',
    'tab:orange',
    'tab:green',
    'tab:red',
    'tab:purple',
    'tab:brown',
    'tab:pink',
    'tab:gray',
    'tab:olive',
    'tab:cyan',
]

def show_clusters_centroids(clusters,
                            centroids,
                            title,
                            x_var_indx=0,
                            y_var_indx=1,
                            x_var_name='Variable 1',
                            y_var_name="Variable 2",
                            keep=False):

    """
    Show the current clustering for 1 second and save the plot
    Input:
        clusters (list of lists of lists): A List of Clusters. Each cluster
        is also a list of points in the cluster. SEE: k_means.get_clusters()
        centroids (list of lists): A list with the current centroids
        title (string): The title for the plot.
    """

    for i, cluster in enumerate(clusters):
        cluster = np.array(cluster)
        plt.scatter(
            cluster[:,x_var_indx],
            cluster[:,y_var_indx],
            c = COLORS[i],
            label="Cluster {}".format(i)
        )

    for i, centroid in enumerate(centroids):
        plt.scatter(
            centroid[x_var_indx],
            centroid[y_var_indx],
            c = COLORS[i],
            marker='x',
            s=100
        )

    plt.title(title)
    plt.xlabel(x_var_name)
    plt.ylabel(y_var_name)
    plt.legend()

    if not os.path.isdir('./images/kmeans_out/'):
        os.mkdir('./images/kmeans_out')

    plt.savefig("./images/kmeans_out/kmeans_{}.png".format(title))

    if not keep:
        plt.show(block=False)
        plt.pause(1)
        plt.close()
    else:
        plt.show()
