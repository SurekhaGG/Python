#!/usr/bin/env python
# coding: utf-8

# In[11]:


import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import plotly.express as px

#seaborn package
Xpoints=np.array([0,20,120,200])
Ypoints=np.array([10,80,100,120,150,180,250])
print(sns.scatterplot(data=Ypoints))
print(plt.show())


# In[14]:


print(sns.barplot(data=Ypoints))
print(plt.show())


# In[22]:


#3-D plot
x=np.array([1,2,6,8,12,14,20])
y=np.array([3,8,1,10,12,16,18])
Fig=plt.figure(figsize=(12,8))
ax=plt.axes(projection='3d')
plt_3d=ax.scatter3D(x,y)
plt.colorbar(plt_3d)
plt.show()
#plotly package
X=np.array([10,80,100,120,150,180,250])

fig=px.scatter(x)
fig.show()


# In[ ]:




