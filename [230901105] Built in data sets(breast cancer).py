#!/usr/bin/env python
# coding: utf-8

# In[2]:


from sklearn import datasets
import pandas as pd


# In[3]:


data=datasets.load_breast_cancer()
label_names=data['target_names']
labels=data['target']
feature_names=data['feature_names']
features=data['data']
print("Breast C ancer data:\n",data);


# In[4]:


print("\nLabel names:\n",label_names)


# In[5]:


print("\nLabels:\n",labels)


# In[6]:


print("\nFeature names:\n",feature_names)


# In[7]:


print("\nFeatures:\n",features)


# In[ ]:




