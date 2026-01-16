#!/usr/bin/env python
# coding: utf-8

# Consider three famous American market indices – Dow Jones, S&P 500, and the Nasdaq for the period of 1st of January 2000 until today.

# In[8]:


import numpy as np
import pandas as pd
from pandas_datareader import data as wb
import yfinance as yf
import matplotlib.pyplot as plt


# In[9]:


tickers = ['^DJI', '^GSPC', '^IXIC']

ind_data = pd.DataFrame()

for t in tickers:
    ind_data[t] =  yf.Ticker(t).history(start='2000-1-1')['Close']


# In[10]:


ind_data.head()


# In[11]:


ind_data.tail()


# Normalize the data to 100 and plot the results on a graph. 

# In[12]:


(ind_data / ind_data.iloc[0] * 100).plot(figsize=(15, 6));
plt.show()


# Obtain the simple returns of the indices.

# In[13]:


ind_returns = (ind_data / ind_data.shift(1)) - 1

ind_returns.tail()


# Estimate the average annual return of each index.

# In[7]:


annual_ind_returns = ind_returns.mean() * 250
annual_ind_returns

