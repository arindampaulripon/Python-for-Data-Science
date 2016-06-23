import numpy as np

def euclideanDistanceSquared(x, centers):
    """Calculates the squared Euclidean distance of each data point to each cluster center
    
    Definitions:
        n           : Number of points
        d           : Number of dimensions
        k           : Number of cluster centers
    Input:
        x           : (n x d)
        centers     : (k x d)
        
    Output:
        eucDistSq   : (n x k)
    """
    
    eucDistSq = np.sum((x[:, np.newaxis, :] - centers)**2, axis = 2, dtype=float)
    return eucDistSq