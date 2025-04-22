#!/usr/bin/env python
# coding: utf-8

# In[3]:


from sklearn import datasets
import pandas as pd
iris=datasets.load_iris()
print(iris)
print("\ntype:\n",type(iris))


# In[4]:


print("\nkeys:\n",iris.keys())


# In[5]:


print("\ntype of data and target:\n",type(iris.data),type(iris.target))


# In[7]:


print("\n data shape:\n",iris.data.shape)


# In[8]:


print("\ntarget names:\n",iris.target_names)


# In[9]:


X=iris.data


# In[10]:


Y=iris.target


# In[13]:


df=pd.DataFrame(X,columns=iris.feature_names)
print("\niris dataframe:\n",df.head())
print("-------------------------------------------------\n")


# In[ ]:





# In[ ]:




