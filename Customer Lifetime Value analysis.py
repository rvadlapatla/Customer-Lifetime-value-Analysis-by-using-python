#!/usr/bin/env python
# coding: utf-8

# #                        Customer Lifetime Value Analysis

# Customer lifetime value analysis is used to estimate the total value of customers to the business over the lifetime of their relationship. It helps companies determine how much to invest in customer acquisition and retention, as well as identify the most valuable customers to prioritize for retention efforts.
# 
# By analyzing customer lifetime value, companies can identify the most effective marketing channels and campaigns for acquiring high-value customers, as well as develop targeted retention strategies to keep those customers engaged and loyal.
# 
# For the Customer Lifetime Value analysis task, we need a dataset based on customers’ relationships with the business.

# In[3]:


import pandas as pd
import plotly.express as px
import plotly.graph_objs as go
import plotly.io as pio
pio.templates.default = "plotly_white"


# In[ ]:





# In[4]:


data =pd.read_csv(r"C:\Users\User\Downloads\acquisition_data (1)\customer_acquisition_data.csv")
print(data)


# In[6]:


data.shape


# In[9]:


data.describe()


# In[12]:


fig =px.bar(data,x='cost',y='revenue',title ='Distribution of Acquistion')
fig.update_layout(xaxis_title="cost",yaxis_title='count')
fig.show()


# In[14]:


fig =px.histogram(data,x='cost',nbins=20,title ='Distribution of cost')
fig.update_layout(xaxis_title="cost",yaxis_title='count')
fig.show()


# In[15]:


fig =px.histogram(data,x='revenue',nbins=20,title ='Distribution of Revenue')
fig.update_layout(xaxis_title="cost",yaxis_title='count')
fig.show()


# Now let’s compare the cost of acquisition across different channels and identify the most and least profitable channels:

# In[17]:


channle_cost =data.groupby('channel')['cost'].mean().reset_index()
fig =px.bar(channle_cost,x='channel',y='cost',title ='Cost of channel')
fig.show()


# So paid advertisement is the most expensive channel, and email marketing is the least expensive channel. Now let’s see which channels are most and least effective at converting customers:

# In[18]:


channel_coversation =data.groupby('channel')['conversion_rate'].mean().reset_index()
fig =px.bar(channel_coversation,x='channel',y='conversion_rate',title =" number od customer in channel ")
fig.show()


# Social media is the most effective channel for converting customers, while paid advertising is the least effective. Now let’s calculate the total revenue by channel and have a look at the most and least profitable channels in terms of generating revenue:

# 

# In[21]:


revenue_by_channel = data.groupby('channel')['revenue'].sum().reset_index()
fig =px.pie(revenue_by_channel,values ="revenue",
           names ="channel",
           title ="total Revenue by channel",hole =0.6,color_discrete_sequence =px.colors.qualitative.Pastel)
fig.show()


# In[26]:


data["roi"] =data['revenue']/data['cost']
#print(data['roi'])
roi_channel =data.groupby('channel')['roi'].mean().reset_index()
fig =px.bar(roi_channel,x ='channel',y='roi',title ='Return of Invertment')
fig.show()


# In[33]:


data["cltv"] =(data['revenue'] - data["cost"]) * data['conversion_rate'] / data['cost']
#print(data["cltv"])
channel_cltv =data.groupby("channel")["cltv"].mean().reset_index()
fig =px.bar(channel_cltv,x= "channel",y ="cltv",title = "Customer life time by channel",color ="channel")
fig.update_layout(xaxis_title ="channel",yaxis_title="cltv")

fig.show()


# In[39]:


sub =data.loc[data['channel'].isin(['social media','referral'])]
#print(sub)
fig =px.box(sub,x= "channel",y ="cltv",title = "Customer life time by channel",color ="channel")
fig.update_layout(xaxis_title ="channel",yaxis_title="cltv",legend_title ="Channel")

fig.show()


# In[ ]:




