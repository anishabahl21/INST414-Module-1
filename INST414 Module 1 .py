#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('C:\\Users\\bahla\\Desktop\\INST414\\DataScience_UKJobs.csv')


# In[2]:


top_10_positions = df.head(10)


# In[3]:


top_10_positions


# In[4]:


needed_columns = ['Company', 'Job Title', 'Salary', 'Skills']


# In[5]:


table_subset = top_10_positions[needed_columns]


# In[7]:


table_subset


# In[8]:


plt.figure(figsize = (17,6))
plt.bar(top_10_positions['Job Title'], top_10_positions['Salary'], color = 'red')


# In[9]:


row_highest_paying_job = top_10_positions.iloc[5]


# In[10]:


row_highest_paying_job


# In[12]:


row_highest_paying_job['Skills']

