# %%
import pandas as pd
df_flights = pd.read_csv("../data/raw/flights.csv")
df_flights.head()




# %% [markdown]
# **Clean missing values**
# Find how many null values are there for each column

# %%
df_flights.isnull().sum()

# %% [markdown]
# Departures are considered late if the delay is 15 minutes or more,
# 
# so let's see the delays for the one with a null late indicator:

# %%
df_flights [df_flights.isnull().any(axis=1)][['DepDelay', 'DepDel15']]

# %%
df_flights[df_flights.isnull().any(axis=1)].DepDelay.describe()

# %% [markdown]
# The min, max, and mean are all 0, so it means that none were actually late departures. Let's
# 
# replace the missing DepDel15 indicator with a 0 and confirm there are no missing values.

# %%
df_flights.DepDel15 = df_flights.DepDel15.fillna(0)
df_flights.isnull().sum()


# %% [markdown]
# **Clean Outliers**
# 
# View the distribution and summary statistics for the DepDelay and ArrDelay
# 
# Columns.

# %%
# Function to show summary stats and distribution for a column

def show_distribution (var_data):
    from matplotlib import pyplot as plt
    
    #Get statistics
    min_val = var_data.min()
    max_val = var_data.max()
    mean_val = var_data.mean()
    med_val = var_data.median()
    mod_val = var_data.mode()[0]
    
    print (var_data.name, '\nMinimum:{:.2f}\nMean:{:.2f}\nMedian:{:.2f}\nMode:{:.2f}\nMaximum:{:.2f}\n'.format(min_val,
                                                                                                            mean_val,
                                                                                                            med_val,
                                                                                                            mod_val,
                                                                                                            max_val))
    #Create a figure for 2 subplots (2 rows, 1 column)
    
    fig, ax = plt.subplots(2, 1, figsize = (10, 4))
    
    #Plot the histogram
    ax[0].hist(var_data)
    ax[0].set_ylabel ('Frequency')
    
    #Add lines for the mean, median, mode
    
    ax[0].axvline (x=min_val, color = 'gray', linestyle = 'dashed', linewidth =2)
    ax[0].axvline (x=mean_val, color = 'cyan', linestyle = 'dashed', linewidth =2)
    ax[0].axvline (x=med_val, color = 'red', linestyle = 'dashed', linewidth =2)
    ax[0].axvline (x=mod_val, color = 'yellow', linestyle = 'dashed', linewidth =2)
    ax[0].axvline (x=max_val, color = 'gray', linestyle = 'dashed', linewidth =2)
    
    #Plot the boxplot
    ax[1].boxplot (var_data, vert= False)
    ax[1].set_xlabel('Value')
    
    #Add a title to the Figure
    fig.suptitle (var_data.name)
    
    #Show the figure
    plt.show()
    
#Call the function for each delay field
    
delayFields = ['DepDelay', 'ArrDelay']
for col in delayFields:
    show_distribution(df_flights[col])

    

# %% [markdown]
# There are outliers at the lower and upper ends of both variables - particularly at the upper end.
# 
# Let's trim the data so that we include only rows where the values for these fields are within the 1st and 90th percentile.

# %%
#Trim outliers for ArrDelay based on 1% and 90% percentiles

ArrDelay_01pcntile = df_flights.ArrDelay.quantile(0.01)
ArrDelay_90pcntile = df_flights.ArrDelay.quantile(0.90)

df_flights = df_flights[df_flights.ArrDelay < ArrDelay_90pcntile]
df_flights = df_flights[df_flights.ArrDelay > ArrDelay_01pcntile]

#Trim outliers for DepDelay based on 1% and 90% percentiles

DepDelay_01pcntile = df_flights.DepDelay.quantile(0.01)
DepDelay_90pcntile = df_flights.DepDelay.quantile(0.90)

df_flights = df_flights[df_flights.DepDelay < DepDelay_90pcntile]
df_flights = df_flights[df_flights.DepDelay > DepDelay_01pcntile]

#View the revised distributions
for col in delayFields:
    show_distribution(df_flights[col])


# %% [markdown]
# That looks a bit better.
# 
# **Explore the data**
# 
# Let's start with an overall view of the summary statistics for the numeric column

# %%
df_flights.describe()

# %% [markdown]
# **What are the mean departure and arrival delays**

# %%
df_flights[delayFields].mean()

# %%
for col in delayFields:
    df_flights.boxplot(column=col, by='Carrier', figsize=(8,8))

# %% [markdown]
# **Which departure airport has the highest average departure delay?**

# %%

departure_airport_group = df_flights.groupby (df_flights.OriginAirportName)

mean_departure_delays = pd.DataFrame(departure_airport_group['DepDelay'].mean()).sort_values ('DepDelay', ascending = False)

mean_departure_delays.plot(kind = 'bar', figsize=(12,12))

mean_departure_delays


# %% [markdown]
# **Do late departures tend to result in longer arrival delays than on-time departures**

# %%
df_flights.boxplot (column = 'ArrDelay', by= 'DepDel15', figsize=(12,12))

# %% [markdown]
# **which route (from origin airport to destination airport) has the most late arrivals?**

# %%
# Add a routes column
routes  = pd.Series(df_flights['OriginAirportName'] + ' > ' + df_flights['DestAirportName'])
df_flights = pd.concat([df_flights, routes.rename("Route")], axis=1)

# Group by routes
route_group = df_flights.groupby(df_flights.Route)
pd.DataFrame(route_group['ArrDel15'].sum()).sort_values('ArrDel15', ascending=False)

# %% [markdown]
# **Which route has the highest average arrival delay**

# %%
pd.DataFrame(route_group['ArrDelay'].mean()).sort_values('ArrDelay', ascending = False)


