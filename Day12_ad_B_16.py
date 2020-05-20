#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd


# In[ ]:


#creating a empty dataframe


# In[4]:


df=pd.DataFrame()
print(df)


# In[ ]:


#creating a df from list:


# In[5]:


data=['Ram','Ram2','jawahar','hameed']


# In[6]:


df=pd.DataFrame(data)
print(df)


# In[10]:


data=[['aishwarya',10],['harshini',8],['shwetha',9],['harika',8]]
df=pd.DataFrame(data,columns=['Name','Marks'])
print(df)


# In[11]:


df=pd.DataFrame(data,codata=[['aishwarya',10],['harshini',8],['shwetha',9],['harika',8]]
lumns=['Name','Marks'],dtype=float)
print(df)


# In[ ]:


#enhancement of the code:


# In[14]:


data=[['aishwarya',10],['harshini',8],['shwetha',9],['harika',8]]
df=pd.DataFrame(data,columns=['Name','Marks'],index=['rank1','rank3','rank2','rank3'])
print(df)


# In[ ]:


#creating a dataframe from dictionary:


# In[15]:


data={'Name':['bikesh','naveen','srinu','chandu','ravi'],'age':[25,24,19,21,26]}


# In[17]:


df=pd.DataFrame(data)
print(df)


# In[23]:


data=[['jyosthna','chicken','black'],['harika','biryani','blue'],['manisha','pizza','red']]


# In[24]:


df=pd.DataFrame(data,columns=['Name','Food','Favcolor'],index=[1,2,3])


# In[25]:


print(df)


# In[27]:


data={'name':['jyosthna','harika','manisha'],'food':['chicken','biryani','pizza'],'favcolor':['black','blue','red']}
df=pd.DataFrame(data,index=[1,2,3])
print(df)


# In[ ]:




