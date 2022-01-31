#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


def estimators(estimates, params):
    """
    Input: Sequences of IDs for (kappa, Np) combinations which have been
    identified as estimators by the method.
    
    Output: DataFrame of estimates kappa_hat and Np_hat given a time window t
    
    The function matches the ids of the parameter combination with the ML
    estimators (kappa_hat and Np_hat).
    """
    kappa_seq = []
    np_seq = []
    for combs in estimates["params"]:
        kappa,np = params[combs]
        kappa_seq.append(kappa)
        np_seq.append(np)
    return kappa_seq,np_seq

