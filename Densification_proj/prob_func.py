#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
from numba import njit


# In[2]:


@njit()
def prob_func(A,E,likelihood):
    
    """
        A - active banks (type:float)
        E - number of undirected edges (type:float)
        likelihood - likelihood function given a kappa and Np,
        (type: B x 3 numpy array, where B is the number combinations of N,M generated from 
        kappa and Np)
        Returns the probability of observing A and E given a kappa and Np.
    """
    
    probindex = np.where((likelihood[0:,0]==A) & (likelihood[0:,1]==E))
    if probindex[0].size!=0:
        probability = likelihood[probindex][0,-1]
    
    return probability

