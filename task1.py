#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt

# Sample data - Replace with your actual dataset (e.g., population data over the years)
# Here's an example with made-up population data over 10 years.
years = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019]
population = [6750000000, 6810000000, 6870000000, 6930000000, 6990000000,
              7050000000, 7110000000, 7170000000, 7230000000, 7290000000]

# Create a DataFrame from the data
data = pd.DataFrame({
    'Year': years,
    'Population': population
})

# Plot a bar chart to show population distribution over the years
plt.figure(figsize=(10, 6))
plt.bar(data['Year'], data['Population'], color='skyblue')

# Add titles and labels
plt.title('Population Distribution Over the Years', fontsize=14)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Population (in billions)', fontsize=12)

# Display the chart
plt.show()
