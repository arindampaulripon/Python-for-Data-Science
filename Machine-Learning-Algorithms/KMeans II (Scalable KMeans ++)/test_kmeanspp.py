import numpy as np
from kMeansPlusPlusFunc import kMeansPlusPlus
from scalableKMeansPlusPlusFunc import scalableKMeansPlusPlus

def test_length():
    data = np.random.normal(size=(2000,2))
    k = 3
    l = 5
    kCenters1 = kMeansPlusPlus(data, k)
    kCenters2 = scalableKMeansPlusPlus(data, k, l)
    assert len(kCenters1)==k and len(kCenters2)==k