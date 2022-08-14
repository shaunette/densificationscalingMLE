#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd
import numpy as np


# In[6]:


PARCOMBS_LOC = "/DIRECTORY_NAME/parameter_combinations/paramcombs.csv"
LKFNS_LOC = "/DIRECTORY_NAME/likelihoodfns/Likefn"


# In[7]:


#1 User imports the Dictionary of parameter combinations. Format - ID: (kappa, Np)
parcombs = pd.read_csv(PARCOMBS_LOC)
parcombs_dict = parcombs.set_index("id").T.to_dict("list")
parcombs2 = {key:tuple(values) for key, values in parcombs_dict.items()}


# In[8]:


#2 User imports the likelihood functions
Likelihoodfns = {}
for combs in parcombs2:
    df = pd.read_pickle(LKFNS_LOC+combs)
    Likelihoodfns[combs] = df[["N","M","prob"]].values

