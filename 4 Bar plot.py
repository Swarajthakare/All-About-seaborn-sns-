#!/usr/bin/env python
# coding: utf-8

# In[20]:


import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt


# In[2]:


tips_df = sns.load_dataset("tips")
tips_df


# ### sns.barplot()
# - tips_df.total_bill = accessing columne from data set

# In[3]:


sns.barplot(x = tips_df.total_bill)


# - tips is catagorical data type and bill is numeric data type 
# - finding corelation between both
# - columns means variable

# In[7]:


sns.barplot(x = tips_df.day, y = tips_df.total_bill)


# In[8]:


sns.barplot(x = tips_df.day, y = tips_df.total_bill, hue = tips_df.sex)


# ### data

# In[9]:


sns.barplot(x = 'day', y = 'total_bill', hue = 'sex',
           data = tips_df)


# ### order use to manage bars acording to your self

# In[10]:


order = ['Sun','Thur','Fri','Sat']
sns.barplot(x = 'day', y = 'total_bill', hue = 'sex',
           data = tips_df, order = order)


# In[11]:


hue_order = ['Female','Male']
sns.barplot(x = 'day', y = 'total_bill', hue = 'sex',
           data = tips_df, hue_order = hue_order)


# ### estimator

# In[16]:


sns.barplot(x = 'day', y = 'total_bill', hue = 'sex',
           data = tips_df, estimator = np.mean)


# In[17]:


sns.barplot(x = 'day', y = 'total_bill', hue = 'sex',
           data = tips_df, estimator = np.max)


# #### ci = confidence intervle

# In[21]:


sns.barplot(x = 'day', y = 'total_bill', hue = 'sex',
           data = tips_df, ci = 12)
plt.show()


# In[22]:


sns.barplot(x = 'day', y = 'total_bill', hue = 'sex',
           data = tips_df, ci = 20)
plt.show()


# In[26]:


sns.barplot(x = 'day', y = 'total_bill', hue = 'sex',
           data = tips_df, estimator = np.max, n_boot = 2)
plt.show()


# #orient = if your data has catgorical variale then you cant plot horizontal

# In[30]:


sns.barplot(x = 'day', y = 'total_bill', hue = 'sex',
           data = tips_df, orient = 'v')
plt.show()


# #if you want to plot horizontal then swich the x y vlaue.
# - no orient use

# In[32]:


sns.barplot(y = 'day', x = 'total_bill', hue = 'sex',
           data = tips_df,)
plt.show()


# In[34]:


#used numeric data variable


# In[35]:


sns.barplot(x = 'total_bill', y = 'size', hue = 'sex',
           data = tips_df, orient = 'h')
plt.show()


# ### color = 

# In[36]:


sns.barplot(x = 'day', y = 'total_bill', hue = 'sex',
           data = tips_df, color = 'g')
plt.show()


# In[37]:


sns.barplot(x = 'day', y = 'total_bill', hue = 'sex',
           data = tips_df, palette = 'hot')
plt.show()


# In[38]:


sns.barplot(x = 'day', y = 'total_bill', hue = 'sex',
           data = tips_df, palette = 'magma')
plt.show()


# In[39]:


sns.barplot(x = 'day', y = 'total_bill', hue = 'sex',
           data = tips_df, saturation = 3)
plt.show()


# In[41]:


sns.barplot(x = 'day', y = 'total_bill', hue = 'sex',
           data = tips_df, errcolor = '0.5')
plt.show()


# In[42]:


sns.barplot(x = 'day', y = 'total_bill', hue = 'sex',
           data = tips_df, errwidth = 12)
plt.show()


# In[44]:


sns.barplot(x = 'day', y = 'total_bill', hue = 'sex',
           data = tips_df, capsize = 1)
plt.show()


# In[46]:


sns.barplot(x = 'day', y = 'total_bill', hue = 'sex',
           data = tips_df, dodge = False) #to overlap bars
plt.show()


# In[ ]:




