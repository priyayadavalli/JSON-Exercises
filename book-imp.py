
# coding: utf-8

# In[67]:


import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import matplotlib
get_ipython().magic('matplotlib inline')
import seaborn as sns
data = pd.read_csv("Desktop/Python/startup_funding.csv")
print(data.shape)
def get_CityWise():
    print("Information on data, Citywise")
    cityNames = data['CityLocation']
    cityNames=cityNames.dropna()
    citygroups=data[['CityLocation','AmountInUSD']].groupby('CityLocation').agg(['count'])
    fig_ops,((ax1))=plt.subplots(1,1,sharex=True)
    cities = citygroups['AmountInUSD','count'].sort_values(ascending=False)
    cities.head(15).plot(kind='bar',title='Number of startups funded City in India',ax=ax1,grid=True,rot=90)


# In[55]:


get_CityWise()


# In[56]:


def get_IndustryVerticalWise():
    print("Information on data, IndustryVertical")
    cityNames = data['IndustryVertical']
    cityNames=cityNames.dropna()
    citygroups=data[['IndustryVertical','AmountInUSD']].groupby('IndustryVertical').agg(['count'])
    fig_ops,((ax1))=plt.subplots(1,1,sharex=True,facecolor='w')
    cities = citygroups['AmountInUSD','count'].sort_values(ascending=False)
    cities.head(15).plot(kind='line',title='Rate of growth to fund IndustryVertical',ax=ax1,grid=True,rot=90)


# In[57]:


get_IndustryVerticalWise()


# In[58]:


def get_InvestmentTypewise():
    print("Information on data, InvestmentType")
    investmentType = data['InvestmentType']
    investmentType=investmentType.dropna()
    investmentgroups=data[['InvestmentType','AmountInUSD']].groupby('InvestmentType').agg(['count'])
    fig_ops,((ax1))=plt.subplots(1,1,sharex=True)
    investmentType = investmentgroups['AmountInUSD','count'].sort_values(ascending=False)
    investmentType.head(15).plot(kind='density',title='Amount distribution for investors',ax=ax1,rot=90)


# In[59]:


get_InvestmentTypewise()


# In[60]:


def get_TopInvestors():
    print("Information on Top Investors")
    investorsName=data['InvestorsName']
    investorsName=investorsName.dropna()
    investorsGroup=data[['InvestorsName','AmountInUSD']].groupby('InvestorsName').agg(['count'])
    fig_ops,((ax1))=plt.subplots(1,1,sharex=True,facecolor='w')
    investorsName=investorsGroup['AmountInUSD','count'].sort_values(ascending=False)
    investorsName.head(15).plot(kind='area',title='Top Investors in Startups in India',ax=ax1,rot=90)


# In[61]:


get_TopInvestors()


# In[62]:


def get_InvestorName():
 print("Information on data, InvestorName")
 cityNames = data['InvestorsName']
 cityNames=cityNames.dropna()
 citygroups=data[['InvestorsName','AmountInUSD']].groupby('InvestorsName').agg(['count'])
 fig_ops,((ax1))=plt.subplots(1,1,sharex=True,facecolor='w')
 cities = citygroups['AmountInUSD','count'].sort_values(ascending=False)
 cities.head(25).plot(kind='bar',title='Investor Name Data',ax=ax1,grid=True,rot=90)


# In[63]:


get_InvestorName()


# In[64]:


print("Mean median and mode of investments")
data["AmountInUSD"] = data["AmountInUSD"].apply(lambda x: float(str(x).replace(",","")))

print("Min Amount")
print(data["AmountInUSD"].min())
print("Mean Amount")
print(round(data["AmountInUSD"].mean(),2))
print("Median Amount")
print(data["AmountInUSD"].median())
print("Max Amount")
print(data["AmountInUSD"].max())
print("Standard Deviation Amount")
print(round(data["AmountInUSD"].std(),2))


# In[65]:


plt.figure(figsize=(8,5))
sns.distplot(data['AmountInUSD'].dropna())
plt.xlabel('log of Amount in USD', fontsize=12)
plt.title("Log Hist of investment in USD", fontsize=16)
plt.show()


# In[66]:


print('More clear representation of above figure')
data['AmountInUSD_log'] = np.log(data["AmountInUSD"] + 1)
sns.distplot(data['AmountInUSD_log'].dropna())
plt.xlabel('log of Amount in USD', fontsize=12)
plt.title("Log Hist of investment in USD", fontsize=16)
plt.show()

