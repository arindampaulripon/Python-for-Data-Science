import numpy as np
from numpy.testing import assert_almost_equal
from distance_func import distance
from kmeanspp_func import cost, sample_new, distribution

def test_length():
    data = np.random.normal(size=(20,4))
    centroids = data[np.random.choice(range(4),4),]
    dist = distance(data,centroids)
    c = cost(dist)
    p = distribution(dist,c)
    l = 5
    c_new = sample_new(data,p,l)
    assert len(c_new)==5

def test_in_data():
    data = np.random.normal(size=(20,4))
    centroids = data[np.random.choice(range(4),4),]
    dist = distance(data,centroids)
    c = cost(dist)
    p = distribution(dist,c)
    l = 5
    c_new = sample_new(data,p,l)
    check = [i in data for i in c_new]
    assert all(check)
    