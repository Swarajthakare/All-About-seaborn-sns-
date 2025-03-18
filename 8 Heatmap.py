#!/usr/bin/env python
# coding: utf-8

# # Part 3

# ## feature engineering and feature selection

# ## What is Correlation?
# - A correlation is a statistical measure of the relationship between two variables(x,y)
# - The correlation coefficient is value form -1 to 1.
#  - -1 : Perfect negatice correlation(Ex. X- increases then Y- decreases).
#  - 0 : No correlation (Ex. X - increases no affect on Y and vice versa).
#  - 1 : Perfect positive correlation (Ex. X- increases then Y - increases).
#     
#     
# - formula

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


globalWarming_df = pd.read_csv(r"B:\Worked dataset\Who_is_responsible_for_global_warming (1).csv")
globalWarming_df.head()


# In[3]:


globalWarming_df.corr()


# ### positive co relation one to anathor ^

# In[4]:


plt.figure(figsize = (21,9))
ax = sns.heatmap(globalWarming_df.corr(), annot= True, linewidth = 3)
ax.tick_params(size = 10, color = 'r', labelsize = 12, labelcolor = 'b')
plt.title("heatmap of 'Who is responsible for global warming'", fontsize = 25)
plt.show()


# In[ ]:





# In[5]:


from sklearn.datasets import load_breast_cancer
cancer_dataset = load_breast_cancer()
cancer_dataset


# In[6]:


#'malignant', 'benign' = features


# # converting into data set

# In[7]:


cancer_df = pd.DataFrame(np.c_[cancer_dataset['data'],cancer_dataset['target']],
                        columns = np.append(cancer_dataset['feature_names'],['target']))
cancer_df


# In[8]:


# feature enginnering = finding co relation through visualising


# In[9]:


plt.figure(figsize = (16,9))
sns.heatmap(cancer_df.corr(),annot = True, linewidth = 3)
ax.tick_params(size = 10, color = 'r', labelsize = 10, labelcolor = 'b')
plt.title("heatmap of brest Cancer Patients", fontsize = 25)
plt.show()


# In[ ]:




