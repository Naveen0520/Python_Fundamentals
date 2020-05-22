#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[2]:


df=pd.read_csv('artwork_data.csv',index_col='id')
df


# In[3]:


artists=df['artist']
pd.unique(artists)
len(pd.unique(artists))


# In[8]:


s=df['arists']
df['arists']='Bacon,Francis'
s.value_counts()


# In[9]:


s=df['artist']=='Bacon,Francis'
s.value_counts()


# In[10]:


artist_counts=df['artist'].value_counts()
artist_counts


# In[11]:


s=df['artist']=='Jones,George'
s.value_counts()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




