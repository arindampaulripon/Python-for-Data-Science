import numpy as np
from distanceFunc import euclideanDistanceSquared
from kMeansFunc import kMeans

def cost(sqDistances):
    """ Cost for each data point based on the minimum distance with respect to cluster centers
    
    Input:
        sqDistance : Squared Euclidean Distance between each data point and the cluster centers
    
    Output:
        cost       : The cost (sum of minimum distances) of the data given current cluster centers
    """ 
    return np.sum(np.min(sqDistances, axis = 1))

def samplingDistribution(sqDistances, cost):
    """ Creates a distribution for the sampling of new cluster centers
    
    Input:
        sqDistances          : Array of squared euclidean distances for each point to each cluster
        costs                : Cost of the data given current cluster centers
    
    Output:
        samplingDistribution : The sampling distribution for cluster membership
    """
    return np.min(sqDistances, axis = 1) / cost

def sampleClusterCenters(x, samplingDist, s):
    """ Samples center points based on the sampling distribution
    
    Input:
        x             : (n x d) array of data
        samplingDist  : (1 x n) probability distribution
        s             : Number of samples
        
    Output:
        sampledPoints : sampled center points
    """
    return x[np.random.choice(range(x.shape[0]), s, p = samplingDist), :]

def kMeansPlusPlus(x, k, maxIters = 10000):
    """ KMeans ++ algorithm
    
    Input:
        x       : (n x d) array of data
        k       : Number of clusters
        maxIters : maximum number of iterations
    
    Output:
        iters      : number of iterations to convergence
        kcenters   : final centers of clusters
        labels     : cluster membership of each point
    """
    # Initialize centers
    centers = x[np.random.choice(x.shape[0], 1), :]
    
    while centers.shape[0] < k:
        
        # Get the distances
        eucDistSq = euclideanDistanceSquared(x, centers)
        
        # Compute the cost of the data given current clusters
        currentCost = cost(eucDistSq)
        
        # Calculate the distribution for sampling a new center
        samplingDist = samplingDistribution(eucDistSq, currentCost)
        
        # Sample a new cluster center
        newCenter = sampleClusterCenters(x, samplingDist, 1)
        
        # Sample new cluster points and append to set
        centers = np.append(centers, newCenter, axis = 0)
    
    # Apply KMeans on data and get cluster membership
    iters, kCenters, labels = kMeans(x, centers, k, maxIters)
    
    return iters, kCenters, labels