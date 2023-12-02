#!/usr/bin/env python
# coding: utf-8

# In[23]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import warnings
from datetime import datetime
warnings.filterwarnings('ignore')


# # Loading dataset

# In[24]:


df= pd.read_csv(r"C:\Users\GHANSHYAM MISHRA\Downloads\hotel_bookings 2.csv")


# In[25]:


df


# # Exploratory Data Analysis

# In[26]:


df.tail()


# In[27]:


df.shape


# In[28]:


df.columns


# In[29]:


df.info()


# In[30]:


df['reservation_status_date']


# In[40]:


df['reservation_status_date'] = datetime.strptime


# In[41]:


df['reservation_status_date']


# In[43]:


df.info()


# In[44]:


df.describe(include=object)


# In[50]:


for col in df.describe(include=object).columns:
    print(col)
    print(df[col].unique())
    print('-' * 50)


# In[52]:


df.isnull().sum()


# In[ ]:





# In[61]:


df.isnull().sum()


# In[64]:


df.describe()


# In[65]:


df=df[df['adr']<5000]


# In[66]:


df.describe()


# # Data Analysis and Visualization

# In[75]:


can_per = df['is_canceled'].value_counts(normalize=True)
print(df[col].value_counts())
plt.figure(figsize=(5,4))
plt.title('reservation_status')
plt.bar(['Not canceled','canceled'], df['is_canceled'].value_counts(),edgecolor='k',width=0.7)
plt.show()        


# In[ ]:





# In[76]:


df.columns


# In[79]:


plt.figure(figsize=(8, 4))
ax1 = sns.countplot(x='hotel', hue='is_canceled', data=df, palette='Blues')
legend_labels, _ = ax1.get_legend_handles_labels()
plt.title('Reservation Status in Different Hotels', size=20)


# In[81]:


resort_hotel = df[df['hotel'] == 'Resort Hotel']
resort_hotel['is_canceled'].value_counts(normalize=True)


# In[84]:


city_hotel = df[df['hotel']=='City Hotel']
city_hotel['is_canceled'].value_counts(normalize=True)


# In[85]:


resort_hotel = resort_hotel.groupby('reservation_status_date')[['adr']].mean()
city_hotel =  city_hotel.groupby('reservation_status_date')[['adr']].mean()


# In[95]:


df.columns


# In[ ]:


"
plt.figure(figsize=(20, 8))
plt.title('Average Daily Rate in City and Resort Hotel', fontsize=30)
plt.plot(resort_hotel.index, resort_hotel['adr'], label='Resort_Hotel')
plt.plot(city_hotel.index, city_hotel['adr'], label='city_hotel')
plt.legend(fontsize=20)
plt.show()"


# In[ ]:


"# Convert 'reservation_status_date' column to datetime type
df['reservation_status_date'] = pd.to_datetime(df['reservation_status_date'])

# Create a new 'month' column
df['month'] = df['reservation_status_date'].dt.month

# Plot the data
plt.figure(figsize=(16, 8))
sns.countplot(x='month', hue='is_canceled', data=df)
plt.title('Monthly Cancellation Counts', size=20)
plt.show()
"


# In[ ]:


"df['month'] = df['reservation_status_date'].dt.month
month= df['reservation_status_date'].dt.month
plt.figure(figsize=(16, 8))
ax1 = sns.countplot(x='month', hue='is_canceled', data=df, palette='bright')
legend_labels,_= ax1.get_legend_handles_labels()
ax1.legend(bbox_to_anchor=(1,1))
plt.title('Reservation status per month',size= 20)
plt.xlable('month')
plt.ylable('number of reservation')
plt.legend(['not canceled','canceled'])
plt.show()"


# In[ ]:





# In[ ]:





# In[ ]:


"plt.figure(figsize = (15,8))
plt.title('ADR per month', fontsize = 30)
sns.barplot('meal','adr' , data=df[df['is_canceled'] == 1].groupby('meal')[['adr']].sum().reset_index())
plt.show()"


# In[ ]:





# In[ ]:





# In[ ]:





# In[103]:


plt.figure(figsize=(15, 8))
plt.title('ADR per month', fontsize=30)
sns.barplot(x='meal', y='adr', data=df[df['is_canceled'] == 1].groupby('meal')[['adr']].sum().reset_index())
plt.show()


# In[ ]:





# In[105]:


cancelled_data = df[df['is_canceled'] == 1]
top_10_country = cancelled_data['country'].value_counts()[:10]
plt.figure(figsize = (8,8))
plt.title('Top 10 countries with reservation canceled')
plt.pie(top_10_country,autopct = '%.2f',labels =top_10_country.index)
plt.show()


# In[ ]:





# In[ ]:





# In[ ]:





# In[83]:


df.columns


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




