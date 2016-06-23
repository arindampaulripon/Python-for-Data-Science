import numpy as np
from scipy.stats import multivariate_normal
import scipy
from scipy.special import gamma 
from numpy.testing import assert_almost_equal
from Bayhiecluster import bcluster, marginal_likelihood_NIW, yezi

#parameters for test data
mean0=(0,0)
cov0=np.eye(2)

mean2=(0,0)
cov2=0.5*np.eye(2)

mean3=(2,2)
cov3=0.5*np.eye(2)

mean4=(8,8)
cov4=0.5*np.eye(2)


def test_atleast_onecluster():
    for i in range(20):
        data2=np.random.multivariate_normal(mean2,cov2,3)
        data3=np.random.multivariate_normal(mean3,cov3,4)
        data4=np.random.multivariate_normal(mean4,cov4,3)
        sample_NIW=np.concatenate((data2, data3,data4), axis=0)
        k,l=bcluster(sample_NIW,marginal_likelihood_NIW)
        assert len(l) >= 1
    
def test_max_cluster_number():
    for i in range(20):
        data2=np.random.multivariate_normal(mean2,cov2,3)
        data3=np.random.multivariate_normal(mean3,cov3,4)
        data4=np.random.multivariate_normal(mean4,cov4,3)
        sample_NIW=np.concatenate((data2, data3,data4), axis=0)
        k,l=bcluster(sample_NIW,marginal_likelihood_NIW)
        n=len(sample_NIW)
        assert len(l) <= n
        
def test_if_all_the_same():
    data0=np.random.multivariate_normal(mean0,cov0,1)
    sample0=np.concatenate((data0, data0, data0, data0, data0, data0, data0, data0, data0, data0), axis=0)
    k,l=bcluster(sample0,marginal_likelihood_NIW)
    assert len(l) == 1
    
def test_only_one_point():
    special=[[np.random.multivariate_normal(mean0,cov0,1)]]
    k,l=bcluster(special,marginal_likelihood_NIW)
    assert len(l) == 1