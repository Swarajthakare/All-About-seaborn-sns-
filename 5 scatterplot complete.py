#!/usr/bin/env python
# coding: utf-8

# In[1]:


import seaborn as sns
import matplotlib.pyplot as plt


# In[2]:


titanic_df = sns.load_dataset("titanic")
titanic_df


# In[3]:


sns.scatterplot(x = "age", y = "fare", data = titanic_df)


# In[4]:


sns.scatterplot(x = "age", y = "fare", data = titanic_df, hue = "sex")


# In[5]:


sns.scatterplot(x = "age", y = "fare", data = titanic_df, hue = "sex",
               style = "who")


# In[6]:


sns.scatterplot(x = "age", y = "fare", data = titanic_df, hue = "sex",
               style = "who", size = "who")


# In[7]:


sns.scatterplot(x = "age", y = "fare", data = titanic_df, hue = "sex",
               style = "who", size = "who", sizes = (100,400))


# In[8]:


plt.figure(figsize = (16,9))
sns.scatterplot(x = "age", y = "fare", data = titanic_df, hue = "sex",
               style = "who", size = "who", sizes = (100,400))


# In[ ]:





# In[9]:


plt.figure(figsize = (16,9))
sns.scatterplot(x = "who", y = "fare", data = titanic_df, hue = "alive",
               style = "alive", size = "who", sizes = (100,400))


# In[10]:


plt.figure(figsize = (16,9))
sns.scatterplot(x = "who", y = "fare", data = titanic_df, hue = "alive",
               style = "alive", size = "who", sizes = (100,400),
               palette = "inferno_r", alpha = 0.7)


# In[11]:


plt.figure(figsize = (16,9)),
sns.scatterplot(x = "age",y = "fare", data = titanic_df)
sns.lineplot(x = "age", y = "fare", data = titanic_df)
sns.barplot(x = "age", y = "fare", data = titanic_df)
plt.show()


# In[ ]:




