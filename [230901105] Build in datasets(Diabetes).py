#!/usr/bin/env python
# coding: utf-8

# In[2]:


from sklearn import datasets
import pandas as pd


# In[3]:


diabetes=datasets.load_diabetes()
print("\ndiabetes dataset:\n",diabetes);


# In[5]:


X=diabetes.data
Y=diabetes.target
df=pd.DataFrame(X,columns=diabetes.feature_names)
print("\nDiabetes dataframe:\n",df.head())
print("-------------------------------------------------------\n")


# In[ ]:




