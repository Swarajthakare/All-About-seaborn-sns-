#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


from sklearn.datasets import load_breast_cancer
cancer_dataset = load_breast_cancer()
cancer_dataset


# ### 'malignant' means 0 = cancer, 
# ### 'benign' means 1 = No cancer

# ### creating DataFrame

# In[3]:


cancer_df = pd.DataFrame(np.c_[cancer_dataset['data'],cancer_dataset['target']],
                        columns = np.append(cancer_dataset['feature_names'],['target']))
cancer_df

sns.pairplot(
    data,
    *,
    hue=None,
    hue_order=None,
    palette=None,
    vars=None,
    x_vars=None,
    y_vars=None,
    kind='scatter',
    diag_kind='auto',
    markers=None,
    height=2.5,
    aspect=1,
    corner=False,
    dropna=False,
    plot_kws=None,
    diag_kws=None,
    grid_kws=None,
    size=None,
)
# In[ ]:





# In[4]:


#sns.pairplot(cancer_df)


# In[5]:


sns.pairplot(cancer_df, vars = ['mean smoothness', 'mean compactness', 'mean concavity',
        'mean concave points', 'mean symmetry'])


# In[6]:


# hue = 


# In[14]:


sns.pairplot(cancer_df, vars = ['mean smoothness', 'mean compactness', 'mean concavity',
        'mean concave points', 'mean symmetry'], hue = 'target')


# In[15]:


# hue_order = 


# In[16]:


sns.pairplot(cancer_df, vars = ['mean smoothness', 'mean compactness', 'mean concavity',
        'mean concave points', 'mean symmetry'], hue = 'target', hue_order = [1.0,0.0])


# In[17]:


#palette - 


# In[18]:


sns.pairplot(cancer_df, vars = ['mean smoothness', 'mean compactness', 'mean concavity',
        'mean concave points', 'mean symmetry'], hue = 'target', palette = 'Dark2')


# In[19]:


# seprate variable 


# In[21]:


sns.pairplot(cancer_df, vars = ['mean smoothness', 'mean compactness', 'mean concavity',
        'mean concave points', 'mean symmetry'], hue = 'target', x_vars = ['mean smoothness', 'mean compactness'], y_vars = ['mean concavity'] 


# In[ ]:


# kind - linear 


# In[ ]:


sns.pairplot(cancer_df, vars = ['mean smoothness', 'mean compactness', 'mean concavity',
        'mean concave points', 'mean symmetry'], hue = 'target', kind = 'reg')


# In[ ]:


# marker = 


# In[ ]:


sns.pairplot(cancer_df, vars = ['mean smoothness', 'mean compactness', 'mean concavity',
        'mean concave points', 'mean symmetry'], hue = 'target', marker = ['*',"<"])


# In[ ]:


# height - 


# In[ ]:


sns.pairplot(cancer_df, vars = ['mean smoothness', 'mean compactness', 'mean concavity',
        'mean concave points', 'mean symmetry'], hue = 'target', height = 20)


# In[ ]:





# In[ ]:




