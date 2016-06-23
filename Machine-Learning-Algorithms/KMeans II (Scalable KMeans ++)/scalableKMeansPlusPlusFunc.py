import numpy as np
from distanceFunc import euclideanDistanceSquared
from kMeansPlusPlusFunc import cost, samplingDistribution, sampleClusterCenters
from kMeansFunc import kMeans

def computeWeights(sqDistances, centers):
    """ Compute the weights of each center based on number of data points closest to each center
    
    Input:
        x         : (n x d) array of data
        centers   : (1 x k) array of centers
        
    Output:
        weights   : (1 x n) array of weights
    """
    
    # Get the closest cluster for each data point
    closestCluster = np.argmin(sqDistances, axis = 1)
    
    # Get the number of points closest to each cluster
    _, closestCount = np.unique(closestCluster, return_counts = True)
    #
    #closestCluster = np.zeros(sqDistances.shape)
    #closestCluster[range(sqDistances.shape[0]), np.argmin(sqDistances, axis = 1)] = 1
    #closestCount = np.array([np.count_nonzero(closestCluster[:, i]) for i in range(centers.shape[0])])
    
    # Return the weights
    return closestCount/np.sum(closestCount)

def weightedKMeans(x, centers, k, weights, maxIters = 10000):
    """ KMeans algorithm that utilizes weights for clustering
    
    Definitions:
        n        : Number of points
        d        : Number of dimensions
        
    Input:
        x        : (n x d) array of data
        centers  : (k x d) array of cluster centers
        k        : number of clusters
        weights  : (1 x k) weights
        maxIters : maximum number of iterations
        
    Returns:
        iters      : number of iterations to convergence
        centers    : final centers of clusters
        labels     : cluster membership of each point
    """
    
    n = x.shape[0]
    iters = 0
    
    while iters < maxIters:
        eucDist = euclideanDistanceSquared(x, centers) * weights[: , np.newaxis]
        
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
        
    return centers

def scalableKMeansPlusPlus(x, k, s, maxIters = 10000):
    centers = x[np.random.choice(range(x.shape[0]), 1), :]
    initDistances = euclideanDistanceSquared(x, centers)
    initCost = cost(initDistances)
    
    logCost = int(np.ceil(np.log(initCost)))

    for i in range(logCost):
        # Get the distane between data and centroids
        eucDistSq = euclideanDistanceSquared(x, centers)
        
        # Compute the cost of the data given current clusters
        currentCost = cost(eucDistSq)
        
        # Calculate the distribution for sampling a new center
        samplingDist = samplingDistribution(eucDistSq, currentCost)
        
        # Sample a new cluster center
        newCenter = sampleClusterCenters(x, samplingDist, 1)
        
        # Sample new cluster points and append to set
        centers = np.append(centers, newCenter, axis = 0)
    
    # Reduce (k * l) to k Clusters using KMeans ++
    eucDist = euclideanDistanceSquared(x, centers)
    weights = computeWeights(eucDist, centers)
    initCenters = centers[np.random.choice(range(len(weights)), k, replace = False), :]
    
    # Apply KMeans on data and get cluster membership
    centers = weightedKMeans(centers, initCenters, k, weights, maxIters)
    
    iters, kCenters, labels = kMeans(x, centers, k, maxIters)
    
    return iters, kCenters, labels