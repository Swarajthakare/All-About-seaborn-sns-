#!/usr/bin/env python
# coding: utf-8

# 

# In[14]:


import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from scipy.stats import norm


# In[2]:


tips_df = sns.load_dataset("tips")
tips_df


# In[4]:


sns.distplot(tips_df["size"]) 
#line plot with bar means kernal dencity estimater


# In[5]:


sns.distplot(tips_df["tip"]) 


# In[6]:


sns.distplot(tips_df["total_bill"]) 


# ### parameter =  bins, 

# ### bins = bars

# In[9]:


sns.distplot(tips_df["total_bill"],bins = 10) 


# In[10]:


sns.distplot(tips_df["total_bill"],bins = 100) 


# ### hist = only kernal dencity estimeter (False) 

# In[11]:


sns.distplot(tips_df["total_bill"],hist = False) 


# ### kde = False

# In[12]:


sns.distplot(tips_df["total_bill"], kde = False) 


# ### rug

# In[13]:


sns.distplot(tips_df["total_bill"], rug = True) 


# ### fit = line plot norm means normalise line plot

# In[15]:


sns.distplot(tips_df["total_bill"], fit = norm) 


# hist_kws
# kde_kws
# rug_kws
# fit_kws
# 
# 
# ### color
# 

# In[16]:


sns.distplot(tips_df["total_bill"], color = "r") 


# ### vertical

# In[17]:


sns.distplot(tips_df["total_bill"], vertical = True) 


# ### norm_hist

# In[18]:


sns.distplot(tips_df["total_bill"], norm_hist = True) 


# ### axlabel =

# In[19]:


sns.distplot(tips_df["total_bill"], axlabel = "Total bill swj") 


# ### label =

# In[21]:


sns.distplot(tips_df["total_bill"], label = "Total bill") 
plt.legend()


# In[23]:


sns.distplot(tips_df["total_bill"], label = "Total bill") 

plt.title("Histogram of Total bill")
plt.legend()


# # part 2 of histogram and distplot

# - for background use sns.set() by default its darkgrid

# In[24]:


sns.set()
sns.distplot(tips_df["total_bill"], label = "Total bill") 
plt.legend()


# In[25]:


plt.figure(figsize = (16,9))
sns.set()
sns.distplot(tips_df["total_bill"], label = "Total bill") 
plt.legend()


# ### bins parameter

# - sort_values()

# In[26]:


tips_df.total_bill.sort_values()


# ### bins and xticks
# - xticks() = use for creating bins

# In[32]:


bins = [1,5,10,15,20,25,30,35,40,45,50,55]

plt.figure(figsize = (16,9))
sns.set()

sns.distplot(tips_df["total_bill"], bins = bins) 

plt.xticks(bins)

plt.title("Histogram of Total bill")

plt.show()


# ### hist_kws

# In[35]:


plt.figure(figsize = (16,9))
sns.set()

sns.distplot(tips_df["total_bill"], hist_kws ={"color":"#DC143C", "edgecolor":"#aaff00",
                                              "linewidth":4,"linestyle":"--"} ) 


# ##### alpha:

# In[37]:


plt.figure(figsize = (16,9))
sns.set()

sns.distplot(tips_df["total_bill"], hist_kws ={"color":"#DC143C", "edgecolor":"#aaff00",
                                              "linewidth":4,"linestyle":"--", "alpha": 0.9} ) 


# ### kde_kws

# In[40]:


plt.figure(figsize = (16,9))
sns.set()

sns.distplot(tips_df["total_bill"], 
             hist_kws ={"color":"#DC143C", "edgecolor":"#aaff00",
                        "linewidth":4,"linestyle":"--", "alpha": 0.9},
             kde_kws = {"color": "#8e00ce", "linewidth":8, "linestyle":"--",
                       'alpha':0.9}
            ) 


# ### rug plot

# In[50]:


plt.figure(figsize = (16,9))
sns.set()

sns.distplot(tips_df["total_bill"], 
             hist_kws ={"color":"#DC143C", "edgecolor":"#aaff00",
                        "linewidth":4,"linestyle":"--", "alpha": 0.9},
             
             kde_kws = {"color": "#8e00ce", 
                        "linewidth":8, "linestyle":"--",'alpha':0.9},
             rug = True,
             rug_kws = {"color": "#0426d0", "linewidth":5,
                        "linestyle":"--",'alpha':0.9})  #"edgecolor":"#00dbff",
plt.show()


# ### fit and fit_kws

# In[56]:


plt.figure(figsize = (16,9))
sns.set()

sns.distplot(tips_df["total_bill"], 
             hist_kws ={"color":"#DC143C", "edgecolor":"#aaff00",
                        "linewidth":4,"linestyle":"--", "alpha": 0.9},
             kde = False,
             fit = norm,
             fit_kws = {"color": "#8e00ce", 
                        "linewidth":12, "linestyle":"--",'alpha':0.4},
             rug = True,
             rug_kws = {"color": "#0426d0", "linewidth":5,
                        "linestyle":"--",'alpha':0.9},
            label = "TB") 

plt.title("Histogram of Restorant Total Bill", fontsize = 20)
plt.xlabel("Total bill", fontsize = 15)
plt.legend()
plt.show()


# ### plot multiple histogram home work

# In[ ]:




