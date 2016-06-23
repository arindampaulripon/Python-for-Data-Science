import numpy as np
from distanceFunc import euclideanDistanceSquared

def kMeans(x, centers, k, maxIters = 10000):
    """ Apply the KMeans clustering algorithm
    
    Definitions:
        n        : Number of points
        d        : Number of dimensions
        
    Input:
        x        : (n x d) array of data
        centers  : (k x d) array of cluster centers
        k        : number of clusters
        maxIters : maximum number of iterations
        
    Returns:
        iters      : number of iterations to convergence
        centers    : final centers of clusters
        labels     : cluster membership of each point
    """
    
    n = x.shape[0]
    iters = 0
    
    while iters < maxIters:
        eucDist = euclideanDistanceSquared(x, centers)
        
        # labels for each point based argmin(distance to cluster)
        labels = np.argmin(eucDist, axis = 1)
        
        # compute new cluster centers
        newCenters = np.zeros(centers.shape)
        for cluster in range(k):
            if sum(labels == cluster) == 0:
                newCenters[cluster] = centers[cluster]
            else:
                newCenters[cluster] = np.mean(x[labels == cluster, :], axis = 0)
        
        # check for convergence
        if np.array_equal(centers, newCenters):
            print("Converged in %d" % iters)
            break
        
        centers = newCenters
        iters += 1

    return iters, centers, labels