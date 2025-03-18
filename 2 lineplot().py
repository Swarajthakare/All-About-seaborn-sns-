#!/usr/bin/env python
# coding: utf-8

# In[14]:


import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt


# ### line plot

# In[15]:


# seaborn need data in DataFrame formate


# In[16]:


days = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
temperature = [36.6, 37,37.7,39,40.1,43,43.4,45,45.6,40.1,44,45,46.8,47,47.8]

temp_df = pd.DataFrame({"days":days,"temperature":temperature})

sns.lineplot(x = 'days',y = 'temperature',data = temp_df )
plt.show()


# In[18]:


sns.load_dataset(name = 'tips')


# In[19]:


tips_df = sns.load_dataset("tips")
tips_df


# In[20]:


tips_df.shape


# In[21]:


sns.lineplot(x = "total_bill",y = "tip", data = tips_df)


# In[22]:


sns.lineplot(y = "total_bill",x = "tip", data = tips_df)


# In[23]:


sns.lineplot(x = "tip" ,y = "total_bill", data = tips_df)


# In[24]:


sns.lineplot(x = "tip" ,y = "size", data = tips_df)


# In[25]:


sns.lineplot(x = "size" ,y = "total_bill", data = tips_df)


# # Part 2
# 

# ### hue = need categorical value
# - differntiate

# In[28]:


sns.lineplot(x = "size" ,y = "total_bill", data = tips_df,hue = "sex")


# ### style = different plot for lines

# In[30]:


sns.lineplot(x = "size" ,y = "total_bill", data = tips_df,hue = "sex",
            style = "sex")


# ### palette = use for changing color

# In[31]:


sns.lineplot(x = "size" ,y = "total_bill", data = tips_df,hue = "sex",
            style = "sex",palette = "Accent")


# In[32]:


sns.lineplot(x = "size" ,y = "total_bill", data = tips_df,hue = "sex",
            style = "sex",palette = "hot")


# ### dashes = line without dashes

# In[34]:


sns.lineplot(x = "size" ,y = "total_bill", data = tips_df,hue = "sex",
            style = "sex",palette = "hot", dashes = False)


# ### markers = changing symbols (use in list)

# In[35]:


sns.lineplot(x = "size" ,y = "total_bill", data = tips_df,hue = "sex",
            style = "sex",palette = "hot", dashes = False, 
            markers = ["o","<"])


# ### legend - bydefault brief 
# - no need legend use False

# In[39]:


sns.lineplot(x = "size" ,y = "total_bill", data = tips_df,hue = "sex",
            style = "sex",palette = "hot", dashes = False, 
            markers = ["o","<"], legend = "brief")


# In[40]:


sns.lineplot(x = "size" ,y = "total_bill", data = tips_df,hue = "sex",
            style = "sex",palette = "hot", dashes = False, 
            markers = ["o","<"], legend = "brief")

plt.title("Line Plot",fontsize = 20)
plt.xlabel("Size",fontsize = 15)
plt.ylabel("Total Bill", fontsize = 15)


# ### to hide showing text use plt.show() fuction.

# In[41]:


sns.lineplot(x = "size" ,y = "total_bill", data = tips_df,hue = "sex",
            style = "sex",palette = "hot", dashes = False, 
            markers = ["o","<"], legend = "brief")

plt.title("Line Plot",fontsize = 20)
plt.xlabel("Size",fontsize = 15)
plt.ylabel("Total Bill", fontsize = 15)
plt.show()


# #### sns.set() = to change background color

# In[42]:


sns.set(style = "darkgrid")
sns.lineplot(x = "size" ,y = "total_bill", data = tips_df,hue = "sex",
            style = "sex",palette = "hot", dashes = False, 
            markers = ["o","<"], legend = "brief")

plt.title("Line Plot",fontsize = 20)
plt.xlabel("Size",fontsize = 15)
plt.ylabel("Total Bill", fontsize = 15)
plt.show()


# #### figure size = use tuple

# In[44]:


plt.figure(figsize = (16,9))
sns.set(style = "darkgrid")
sns.lineplot(x = "size" ,y = "total_bill", data = tips_df,hue = "sex",
            style = "sex",palette = "hot", dashes = False, 
            markers = ["o","<"], legend = "brief")

plt.title("Line Plot",fontsize = 20)
plt.xlabel("Size",fontsize = 15)
plt.ylabel("Total Bill", fontsize = 15)
plt.show()


# 

# In[45]:


plt.figure(figsize = (16,9))
sns.set(style = "darkgrid")
sns.lineplot(x = "size" ,y = "total_bill", data = tips_df,hue = "day",
            style = "day",palette = "hot", dashes = False, 
            markers = ["o","<",">","^"], legend = "brief")

plt.title("Line Plot",fontsize = 20)
plt.xlabel("Size",fontsize = 15)
plt.ylabel("Total Bill", fontsize = 15)
plt.show()


# In[ ]:




