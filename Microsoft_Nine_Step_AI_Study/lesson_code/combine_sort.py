#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random
import numpy as np
import re


# In[2]:


def get_random_data(*arg,samples=20):
    np.random.seed(0)
    random.seed(0)
    total_data=np.array([np.random.choice(choice,size=(samples,),replace=True,p=[1.0/len(choice)]*len(choice)) for choice in arg])
    print(total_data)
    combined_data=[''.join(total_data[:,i]) for i in range(samples)]
    return combined_data


# In[3]:


alphas=['A','B','C','D']
numbers=[0,1,2,3,4,5,6,7,8,9,10]
samples=20
combined_data=get_random_data(alphas,numbers,samples=20)
first_sort=sorted(combined_data,key=lambda x:int(re.findall(r'[a-zA-Z]+(\d+)',x)[0]))
print(first_sort)
output=[]
for w in alphas:
    for d in first_sort:
        if w in re.findall(r'([a-zA-Z]+)\d+',d)[0]:
            output.append(d)
print(output)


# In[ ]:




