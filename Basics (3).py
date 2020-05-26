#!/usr/bin/env python
# coding: utf-8

# # Cleaning Data in Phython
# 
# This is practice cleaning data in Python. I will be using a [sample of 50,000 data points](https://www.kaggle.com/orgesleka/used-cars-database/data) regarding used car sales via the German eBay. In this project I will be using the pandas and NumPy libraries. 

# In[2]:


import pandas as pd
import numpy as np

autos = pd.read_csv("autos.csv", encoding = "Latin-1")


# In[9]:


autos


# In[10]:


print(autos.info())
print(autos.head())


# In[12]:


autos.describe(include = 'all')


# The columns number of pictures, postal code, monthOfRegistration, powerPS, yearOfRegistration,  only has one value (0). I will eventually drop that column from the data set. 
# 
# Price and odometer are listed as strings. I will change these to a float. 
# 
# Seller, offerType, abtest, gearbox, and notRepairedDamage only have two unique values. 

# Our dataset has 50,000 entries and 20 columns. Some columns have null values. Most columns are made up of strings. The column names use camelcase instead of snakecase. 

# ### Cleaning pt 1: Converting from strings to numeric
# 
# As mentioned before, both price and odometer columns are strings, but they should be numeric. For both of these columns, I will remove any non-numeric characters and convert the column to a numeric type. I will also rename the odometer column showing the proper units. 

# In[13]:


autos["price"].head()


# For the price column, I will remove the comma and the dollar sign. 

# In[3]:


autos["price"] = autos["price"].str.replace("$", "").str.replace(",", "").astype(float)

autos["price"].head()


# Let's do the same with the odometer column. 

# In[26]:


autos["odometer"].head()


# In[4]:


autos["odometer"] = autos["odometer"].str.replace("km", "").str.replace(",", "").astype(float)

autos.rename({"odometer": "odometer_km"}, axis =1 , inplace = True)

autos["odometer_km"].head()


# I will now look at the odometer_km column in more detail, trying to find outliers. 

# In[14]:


print(autos["odometer_km"].unique().shape)
print('\n')
print(autos["odometer_km"].describe())
print('\n')
print(autos["odometer_km"].value_counts().sort_index(ascending = True))


# Everything looks reasonable for this column. 
# 
# I will now do the same thing for the price column

# In[27]:


print(autos["price"].unique().shape)
print('\n')
# percentile list 
perc =[0.05, .10, .25, 0.50, .75, .90, 0.95]
print(autos["price"].describe(percentiles = perc))
print('\n')
print(autos["price"].value_counts().sort_index(ascending = True).head(15))
print('\n')
print(autos["price"].value_counts().sort_index(ascending = False).head(15))


# Now we see some oddities. We have 1421 instances where the car is listed as being sold for free. We also have 1 instance where the car was sold for 99 million. This seems odd. 
# 
# The median price is 2950. I am going to remove rows with the following conditions: if the price is less than 200 (5th percentile), or is the price is greater than 19,900 (95th percentile). 

# In[29]:


autos = autos[autos["price"].between(200, 19900)]
print('\n')
print(autos["price"].unique().shape)
print('\n')
# percentile list 
perc =[0.05, .10, .25, 0.50, .75, .90, 0.95]
print(autos["price"].describe(percentiles = perc))
print('\n')
print(autos["price"].value_counts().sort_index(ascending = True).head(5))
print('\n')
print(autos["price"].value_counts().sort_index(ascending = False).head(5))


# Our median price is now 2900. We now have 45207 rows in our dataframe. 

# I will now look at the registration year column and try to find outliers. 

# In[37]:


print(autos["yearOfRegistration"].unique().shape)
print('\n')
print(autos["yearOfRegistration"].describe())
print('\n')
print(autos["yearOfRegistration"].value_counts().sort_index(ascending = True).head(5))
print('\n')
print(autos["yearOfRegistration"].value_counts().sort_index(ascending = False).head(5))


# This looks odd. I don't believe that cars were invented in 1001. I will remove all rows outside of these bounds: prior to 1900 and after 2020. 

# In[38]:


autos = autos[autos["yearOfRegistration"].between(1900, 2020)]


# In[40]:


print(autos["yearOfRegistration"].unique().shape)
print('\n')
print(autos["yearOfRegistration"].describe())
print('\n')
print(autos["yearOfRegistration"].value_counts().sort_index(ascending = True).head(5))
print('\n')
print(autos["yearOfRegistration"].value_counts().sort_index(ascending = False).head(5))
print('\n')
print(autos["yearOfRegistration"].value_counts(normalize=True))


# This looks better. It looks like a majority of our cars were registered between 1997-2010. 

# #### Using Aggregation on The Brand Column
# 
#  I will now explore the brand column

# In[46]:


print(autos["brand"].unique().shape)
print('\n')
print(autos["brand"].describe())
print('\n')
print(autos["brand"].value_counts())


# It looks like we have 40 brands. I will aggregate by the top 6 brands. 

# In[71]:


pop_brands = autos["brand"].value_counts()
print(pop_brands[2])
print(pop_brands.index)
print(pop_brands.index[2])
type(pop_brands)

brand_agg = {}
brand_mil = {}

for i in range (0,6):
    brand_bool = autos["brand"] == pop_brands.index[i]
    brand_df = autos[brand_bool]
    mean_price = round(brand_df["price"].mean())
    mean_mileage = round(brand_df["odometer_km"].mean())
    
    brand_agg[pop_brands.index[i]] = mean_price
    brand_mil[pop_brands.index[i]] = mean_mileage
    
brand_agg


# The dictionary above shows the most popular brands and the mean price of each. It looks like Audi, BMW, and Mercedes are the most expensive.
# 
# For these top 6 brands, I will also aggregate to understand the average mileage to see if there is any visible link between mileage and price. 

# In[72]:


brand_mil


# I will now convert both dictionaries into series objects, and then put them into a dataframe. 

# In[77]:


price_series = pd.Series(brand_agg)
print(price_series)
print('\n')
mileage_series = pd.Series(brand_mil)
print(mileage_series)
print('\n')
df = pd.DataFrame(price_series, columns=['mean_price'])
df['mean_mileage'] = mileage_series
df


# From the eyeball test, there doesn't seem to be much of an association between mileage and price. 
