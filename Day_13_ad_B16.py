#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[3]:


df=pd.read_csv('artwork_data.csv')
df


# In[4]:


df=pd.read_csv('artwork_data.csv',nrows=5,index_col='id')
df


# In[7]:


df=pd.read_csv('artwork_data.csv',nrows=5,usecols=['id','artist','title'],index_col='id')
df


# In[16]:


Cols_To_Add=['id','artist','title','medium','year','height']


# In[26]:


df=pd.read_csv('artwork_data.csv',nrows=10,index_col='id',usecols=Cols_To_Add)
df


# In[27]:


df.to_pickle('dataframe.pickle')


# In[28]:


y=pd.read_pickle('dataframe.pickle')
y


# In[ ]:





# In[18]:


Columns=['id','artist','dimensions','width','height','units','inscription']


# In[19]:


df=pd.read_csv('artwork_data.csv',nrows=10,index_col='id',usecols=Columns)
df


# In[22]:


df.to_pickle('dataframe_b16.pickle')


# In[23]:


x=pd.read_pickle('dataframe_b16.pickle')
x


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




