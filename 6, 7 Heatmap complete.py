#!/usr/bin/env python
# coding: utf-8

# ### Heatmap is graphical representaion of 2D (two dimensional) data.
# ### Each data value represent in a matrix and it has special colour.

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


arr_2d = np.linspace(1,5,12).reshape(4,3)
arr_2d


# #### from 2d dimention data set creating heatmap graph
# - heatmap atleast required one argument

# In[3]:


sns.heatmap(arr_2d)


# #### creating heatmap from realworld data set

# In[4]:


globalWarming_df = pd.read_csv(r"B:\Worked dataset\Who_is_responsible_for_global_warming (1).csv")
globalWarming_df


# In[5]:


globalWarming_df = globalWarming_df.drop(columns = ["Country Code", "Indicator Name", "Indicator Code"], axis = 1).set_index("Country Name")
globalWarming_df.head(6)


# In[6]:


plt.figure(figsize = (16,9))
sns.heatmap(globalWarming_df)
plt.show()


# ### changing heatmap side color bar = vmin(minimum), vmax(maximum)

# In[7]:


plt.figure(figsize = (16,9))
sns.heatmap(globalWarming_df, vmin = 0, vmax = 21)


# #### changing color of heatmap = cmap

# In[8]:


plt.figure(figsize = (16,9))
sns.heatmap(globalWarming_df, cmap = "Accent_r" )


# In[9]:


plt.figure(figsize = (16,9))
sns.heatmap(globalWarming_df, cmap = "coolwarm" )


# #### showing value of bar on graph = annot

# In[10]:


plt.figure(figsize = (16,9))
sns.heatmap(globalWarming_df, cmap = "coolwarm", annot = True )


# #### placing another data set value on 1st data set 
# - fmt means data type string = "s", flote = "d"

# In[11]:


arr_2d


# In[12]:


annot_arr = np.array([['a00','a01','a02'],['a10','a11','a12'],['a20','a21','a22'],['a30','a31','a32']])
annot_arr


# In[13]:


sns.heatmap(arr_2d,annot = annot_arr,fmt = 's')


# In[ ]:





# # Part 2
# 

# #### annot_kws = parameters

# In[14]:


plt.figure(figsize = (16,9))
annot_kws = {"fontsize": 10,
            "fontstyle": "italic",
            "color":"k",
            "alpha":0.6,
            "rotation":"vertical",
            "verticalalignment":"center",
            "backgroundcolor":"w"}

sns.heatmap(globalWarming_df, cmap = "coolwarm", annot = True, annot_kws = annot_kws )


# #### linewidth = of heat map

# In[15]:


plt.figure(figsize = (16,9))

sns.heatmap(globalWarming_df, cmap = "coolwarm", annot = True,
           linewidth = 10)


# - linecolor

# In[16]:


plt.figure(figsize = (16,9))

sns.heatmap(globalWarming_df, cmap = "coolwarm", annot = True,
           linewidth = 10, linecolor = "k")


# #### hiding color bar = cbar = False

# In[17]:


plt.figure(figsize = (16,9))
sns.heatmap(globalWarming_df, cbar = False)


# #### hiding labels from x and y axis

# In[18]:


plt.figure(figsize = (16,9))
sns.heatmap(globalWarming_df, cbar = False, xticklabels = False, yticklabels = False)


# #### side color bar keywords = cbar_kws

# In[19]:


plt.figure(figsize = (16,9))
cbar_kws = {"orientation": "horizontal",
            "shrink":1,
            "extend":"min",
            "extendfrac":0.1,
            "ticks":np.arange(0,22),
            "drawedges":True}
sns.heatmap(globalWarming_df, cbar_kws = cbar_kws)


# #### country code
# 

# In[20]:


plt.figure(figsize = (16,9))
country_code = ['USA', 'GBR', 'IND', 'CHN', 'RUS', 'AUS', 'FRA', 'DEU', 'CAN', 'BRA', 'ARG', 'PAK', 'NPL', 'BGD', 'JPN']

sns.heatmap(globalWarming_df, xticklabels = np.arange(0,15,),yticklabels = country_code )


# #### labels

# In[21]:


plt.figure(figsize = (16,9))
ax = sns.heatmap(globalWarming_df)
ax.set(title = "Heatmap of 'Who is responsible for global warming'",
      xlabel = "CO2 emissions (metric tons per capita) Per Year",
      ylabel = "Country Name")

sns.set(font_scale = 5)


# In[ ]:





# # Part 3

# ### feature engineering and feature selection

# ### What is Correlation?
# - A correlation is a statistical measure of the relationship between two variables(x,y)
# - The correlation coefficient is value form -1 to 1.
#  - -1 : Perfect negatice correlation(Ex. X- increases then Y- decreases).
#  - 0 : No correlation (Ex. X - increases no affect on Y and vice versa).
#  - 1 : Perfect positive correlation (Ex. X- increases then Y - increases).
#  
#  
#  - formula
