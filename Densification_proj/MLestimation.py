#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import numpy as np
from numba import njit
import configr


# In[ ]:


@njit()
def prob_func(A,E,likelihood):
    probindex = np.where((likelihood[0:,0]==A) & (likelihood[0:,1]==E))
    if probindex[0].size!=0:
        probability = likelihood[probindex][0,-1]
    return probability


# In[ ]:


def raw_estimators(estimates):
    """
    Input: Helper that takes sequences of IDs for (kappa, Np) combinations which have been
    identified as estimators by the MLE function above.

    Output: DataFrame of estimates kappa_hat and Np_hat given (N,M)

    The function matches the ids of the parameter combination (i.e, params) with the ML
    estimators (kappa_hat and Np_hat).
    """
    parcombs = configr.parcombs2
    kappa_seq = []
    np_seq = []
    for combs in estimates["params"]:
        kappa,np = parcombs[combs]
        kappa_seq.append(kappa)
        np_seq.append(np)
    return kappa_seq,np_seq


# In[2]:


def estimates(NM):
    """
    Input.

    NMseq: Total active nodes (N) and total edges (M) as (N,M).

    Output. 
    Estimates of overall act and pop size: kappa and Np. Type: (pandas.DataFrame)
    """
    likelihood_funcs = configr.Likelihoodfns    
    knp_ests = []
    for elem in NM:
        N,M = elem
        prob_NM = []
        combid = []
        for fid,LF in likelihood_funcs.items():
            prob_NM.append(prob_func(N,M,LF))
            combid.append(fid)
        estparam_index = np.argmax(np.asarray(prob_NM))
        estparams_id = combid[estparam_index]
        knp_ests.append(estparams_id)
            
    estimates = pd.DataFrame({"params":knp_ests})
    kappavalues, npvalues = raw_estimators(estimates)
    estimates["kappa"] = kappavalues
    estimates["np"] = npvalues
    return estimates

