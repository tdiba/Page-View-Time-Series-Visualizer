#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[4]:


df=pd.read_csv(r'/Users/user/Documents/FreeCodeCamp/fcc-forum-pageviews.csv', index_col='date', parse_dates=True)


# In[5]:


df.head()


# In[6]:


# Filter out the top 2.5% and bottom 2.5% of the dataset
df_filtered = df[
    (df['value'] >= df['value'].quantile(0.025)) & 
    (df['value'] <= df['value'].quantile(0.975))
]


# In[7]:


df.head()


# In[8]:


import matplotlib.pyplot as plt


# In[9]:


# Function to draw line plot using Matplotlib
def draw_line_plot(df):
    # Create a copy of the dataframe to avoid changes to the original data
    df_plot = df.copy()
    
    # Plotting
    fig, ax = plt.subplots(figsize=(15, 5))
    ax.plot(df_plot.index, df_plot['value'], color='skyblue', linewidth=1)

    # Title and labels
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')

    # Rotating the x-axis labels for better readability
    plt.xticks(rotation=45)
    
    # Show the plot
    plt.show()

    return fig


# In[10]:


# Call the function to test it
draw_line_plot(df_filtered)


# In[11]:


import matplotlib.dates as mdates
import seaborn as sns
import numpy as np


# In[12]:


# Function to draw bar plot using Matplotlib
def draw_bar_plot(df):
    # Create a copy of the dataframe to avoid changes to the original data
    df_plot = df.copy()
    
    # Prepare data for bar plot
    df_plot['year'] = df_plot.index.year
    df_plot['month'] = df_plot.index.month_name()
    df_plot['month_number'] = df_plot.index.month  # to order the months correctly in the plot

    # Average daily page views for each month grouped by year
    df_bar = df_plot.groupby(['year', 'month', 'month_number']).mean()
    df_bar = df_bar.unstack(level=0)  # Unstack the year for separate columns

    # Sorting by month number to ensure the correct order
    df_bar = df_bar.sort_values(by='month_number')

    # Bar plot
    fig = df_bar['value'].plot(kind='bar', figsize=(15, 5)).figure
    plt.legend(title='Years', labels=[str(year) for year in df_bar['value'].columns])
    plt.xlabel('Months')
    plt.ylabel('Average Page Views')
    plt.title('Average daily page views for each month grouped by year')
    
    # Reformat the month names on the x-axis
    ax = plt.gca()
    ax.set_xticklabels(df_bar.index.get_level_values('month'), rotation=45)
    
    # Show the plot
    plt.show()

    return fig

# Call the function to test it
draw_bar_plot(df_filtered)


# In[13]:


# Function to draw box plots using Seaborn
def draw_box_plot(df):
    # Create a copy of the dataframe to avoid changes to the original data
    df_plot = df.copy()

    # Prepare data for box plots
    df_plot['year'] = df_plot.index.year
    df_plot['month'] = df_plot.index.month
    df_plot['month_str'] = df_plot.index.strftime('%b')  # for month names

    # Sorting by month to ensure the correct order
    df_plot['month_str'] = pd.Categorical(df_plot['month_str'], categories=[
        'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
        ordered=True)

    # Start drawing box plots
    fig, axes = plt.subplots(1, 2, figsize=(20, 10))

    # Year-wise Box plot (Trend)
    sns.boxplot(x='year', y='value', data=df_plot, ax=axes[0])
    axes[0].set_title('Year-wise Box Plot (Trend)')
    axes[0].set_xlabel('Year')
    axes[0].set_ylabel('Page Views')

    # Month-wise Box plot (Seasonality)
    sns.boxplot(x='month_str', y='value', data=df_plot, ax=axes[1])
    axes[1].set_title('Month-wise Box Plot (Seasonality)')
    axes[1].set_xlabel('Month')
    axes[1].set_ylabel('Page Views')

    # Rotating the x-axis labels for better readability
    for ax in axes:
        for label in ax.get_xticklabels():
            label.set_rotation(45)
    
    # Show the plot
    plt.tight_layout()
    plt.show()

    return fig

# Call the function to test it
draw_box_plot(df_filtered)


# In[ ]:





# In[ ]:




