#!/usr/bin/env python
# coding: utf-8

# ## Import Libraries

# In[1]:


import pandas as pd
from datetime import datetime,timedelta
#import datetime as dt
import mplcursors as mplcursors
import plotly.graph_objects as go
import plotly.express as px


# ## Get Bitcoin HIstorical Daily Data

# In[2]:


df_day = pd.read_csv ("INDEX_BTCUSD, D.csv").reset_index()
df_day['date'] = pd.to_datetime (df_day['date'])


# In[3]:


df_day


# ## Define Variables

# In[4]:


dcaamounts = 100
#start = datetime (2010,7,17)
#end =  start + timedelta (weeks =52*11) #datetime (2021,12,14)


# ## Calculation for Hourly

# In[5]:


#### DCA Daily from 2010 -2021
df_day['buy_high'] = dcaamounts / df_day['high']#.iloc[3807:]
df_day['buy_low'] = dcaamounts / df_day['low']#.iloc[3807:]
df_day['buy_open'] = dcaamounts / df_day['open']#.iloc[3807:]
df_day['buy_close'] = dcaamounts / df_day['close']#.iloc[3807:]

df_day = df_day.groupby (df_day['date'].dt.day_name()).sum()


# In[6]:


#### Sum up coins from OHLC
df_day['total'] = df_day['buy_high']+ df_day['buy_low']+ df_day['buy_open']+df_day['buy_close']
df_day = df_day.sort_values (by='total',ascending=True)


# In[7]:


df_day


# ## Plot

# In[8]:


fig = go.Figure()

fig = px.bar(df_day,x=df_day.index,y = df_day['total'],
            color='total',color_continuous_scale='YlGn')
                # go.Bar(name ='High',x=df.index,y = df['buy_high']),
               #  go.Bar(name ='Low',x=df.index,y = df['buy_low']),
                 #go.Bar(name ='Close',x=df.index,y = df['buy_close'])
                 

fig.update_layout(template="plotly_dark",title_x =0.5, title_text='Total Bitcoin Accumulated with DCA $100 Every Day from 2010-2021')
fig.update_traces (texttemplate ='Total coins:{}'.format(df_day['total']),textposition='outside')
mplcursors.cursor(hover=True)
fig.update_xaxes(title="Day")
fig.update_yaxes(title="Total Coins Accumulated",showgrid=True,range=[117000,125000])
fig.show()

