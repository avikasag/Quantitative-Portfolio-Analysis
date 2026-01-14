#!/usr/bin/env python
# coding: utf-8

# ## Calculating the Return of a Portfolio of Securities

# Download data for a portfolio composed of 5 stocks - British Petroleum, Ford, Exxon, Lincoln, and Apple for the period ‘2025-1-1’ until today.

# In[ ]:


get_ipython().run_line_magic('pip', 'install --upgrade --force-reinstall numpy pandas numexpr bottleneck pandas-datareader')
get_ipython().run_line_magic('pip', 'install yfinance')


# In[1]:


import numpy as np
import pandas as pd
from pandas_datareader import data as wb
import yfinance as yf
import matplotlib.pyplot as plt


# Data Extraction from Yahoo

# In[2]:


tickers = ['BP', 'F', 'XOM', 'LNC', 'AAPL']

# Downloading the Data, everytime we run this code
mydata = pd.DataFrame()
for t in tickers:
    mydata[t] = yf.Ticker(t).history(start='2025-01-01')['Close']  


# Data Validation process

# In[3]:


mydata.info()


# In[4]:


mydata.head(10)


# In[5]:


mydata.tail()


# ### Normalization to 100:
# 
# $$
# \frac {P_t}{P_0} * 100
# $$

# Normalize to a hundred and plot the data on a graph (We can apply the .loc() or the .iloc() method). 

# In[6]:


mydata.iloc[0]


# In[7]:


(mydata / mydata.iloc[0] * 100).plot(figsize = (15, 6));
plt.show()


# *****

# ### Calculating the Return of a Portfolio of Securities

# Obtain the simple return of the securities in the portfolio and store the results in a new table.

# In[8]:


returns = (mydata / mydata.shift(1)) - 1
returns.head()


# First, assume we would like to create an equally-weighted portfolio. Create the array, naming it “weights”.

# In[9]:


weights = np.array([0.2, 0.2, 0.2, 0.2, 0.2])


# Obtain the annual returns of each of the stocks and then calculate the dot product of these returns and the weights.

# In[10]:


annual_returns = returns.mean() * 250
annual_returns


# Portfolio's expected annual return

# In[11]:


np.dot(annual_returns, weights)


# Transform the result into a percentage form. 

# In[12]:


pfolio_1 = str(round(np.dot(annual_returns, weights), 5) * 100) + ' %'
print (pfolio_1)


# Now, assume we would like to create an different-weighted portfolio. Create the array, naming it “weights_2”.

# In[13]:


weights_2 = np.array([0.4, 0.2, 0.2, 0.15, 0.05])


# In[14]:


pfolio_2 = str(round(np.dot(annual_returns, weights_2), 5) * 100) + ' %'
print (pfolio_1)
print (pfolio_2)

