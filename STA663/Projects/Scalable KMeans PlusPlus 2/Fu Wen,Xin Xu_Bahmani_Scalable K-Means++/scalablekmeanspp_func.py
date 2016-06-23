import numpy as np
from distance_func import distance
from kmeanspp_func import cost, distribution, sample_new

def get_weight(dist,centroids):
    """ Get the weight of each centroid
    
    Parameters:
    dist      matrix of distance between data and current centroids
    centroids current centroids
    
    Returns weight of each centroid
    """
    min_dist = np.zeros(dist.shape)
    min_dist[range(dist.shape[0]), np.argmin(dist, axis=1)] = 1
    count = np.array([np.count_nonzero(min_dist[:, i]) for i in range(centroids.shape[0])])
    return count/np.sum(count)

def weightedKMeans(data, k, weight, centroids, max_iter = 10000): 
    
    """ Apply the weighted KMeans clustering algorithm
    
    Parameters:
      data                        ndarrays data 
      k                           number of cluster
      weight                      weight matrix of data
      centroids                   initial centroids
    
    Returns:
      "Iteration before Coverge"  time used to converge
      "Centroids"                 the final centroids finded by KMeans    
      "Labels"                    the cluster of each data   
    """
    
    n = data.shape[0] 
    iterations = 0
    
    while iterations < max_iter:        
        dist = distance(data, centroids) * weight[:, np.newaxis]
        
        ## give cluster label to each point 
        cluster_label = np.argmin(dist, axis=1)
        
        ## calculate new centroids
        newCentroids = np.zeros(centroids.shape)
        for j in range(0, k):
            if sum(cluster_label == j) == 0:
                newCentroids[j] = centroids[j]
            else:
                newCentroids[j] = np.mean(data[cluster_label == j, :], axis=0)
        
        ## Check if it is converged
        if np.array_equal(centroids, newCentroids):
            print("Converge")
            break 
        
        centroids = newCentroids
        iterations += 1
        
    return(centroids)

def ScalableKMeansPlusPlus(data, k, l, weighted=False, iter=5):
    
    """ Apply the KMeans|| clustering algorithm   
    Parameters:
      data     ndarrays data 
      k        number of cluster
      l        number of point sampled in each iteration
      weighted if True, using weighted reclustering in the last step 
                  else, using weighted sampling in the last step.
    
    Returns:   the initial centroids finded by KMeans||  
      
    """
    
    centroids = data[np.random.choice(range(data.shape[0]),1), :]
    
    
    for i in range(iter):
        #Get the distance between data and centroids
        dist = distance(data, centroids)
        
        #Calculate the cost of data with respect to the centroids
        norm_const = cost(dist)
        
        
        #Calculate the distribution for sampling l new centers
        p = distribution(dist,norm_const)
        
        #Sample the l new centers and append them to the original ones
        centroids = np.r_[centroids, sample_new(data,p,l)]
    

    ## reduce k*l to k using KMeans++ 
    dist = distance(data, centroids)
    weights = get_weight(dist, centroids)
    if weighted:
        initial = centroids[np.random.choice(range(len(weights)),k,replace=False),:]
        centers=  weightedKMeans(centroids, k, weights, initial)
    else: 
        centers= centroids[np.random.choice(len(weights), k, replace= False, p = weights),:]
    return centers