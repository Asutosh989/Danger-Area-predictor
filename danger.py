
# coding: utf-8

# # Danger Area Predictor
# 
# [** The Global Terrorism Dataset**](https://www.kaggle.com/START-UMD/gtd) provides us with the information with all the Terrorist Attacks all over world between 1970-2016. It gives very detailed information about the attack like Date, Place, Country, City, Region, Attacktype, Target of Terrorists and Terrorist organizations involved.
# 
# Here our aim is to take the GPS location of the user and alert him if he is in a *Danger Area* or in a *Safe area*, and if he is in a danger area, then which country and what is the nearby danger prone area.

# In[1]:

import pandas as pd
import numpy as np
import plotly.plotly as py
import plotly
from plotly.graph_objs import *


# ##### Here the dataset is imported. And required columns are imported

# In[2]:

gtd = pd.read_csv('gtd_new.csv',usecols=[1,2,3,8,10,12,13,14],low_memory=False,header=0)
gtd = gtd.dropna(axis=0, how = 'any')


# In[3]:

df_2016 = gtd[gtd['iyear']==2016]
df_2016.head()


# In[4]:

df_2015 = gtd[gtd['iyear']==2015]
df_2015.head()


# In[5]:

df_2014 = gtd[gtd['iyear']==2014]
df_2014.head()


# In[6]:

lat_2016 = df_2016['latitude']
lon_2016 = df_2016['longitude']


# In[7]:

lat_2015 = df_2015['latitude']
lon_2015 = df_2015['longitude']


# In[8]:

lat_2014 = df_2014['latitude']
lon_2014 = df_2014['longitude']


# In[9]:

plotly.tools.set_credentials_file(username='Asutosh989', api_key='bdqfWrjiSHQF7t1M8euj')


# In[10]:

country = df_2016['country_txt']
city = df_2016['city']


# In[11]:

lat_l=list(lat_2016)
lon_l=list(lon_2016)
coord = []
for i in range(len(lat_l)):
    coord.append([lat_l[i],lon_l[i]])


# ### Haversine Distance
# Here haversine distance is calculated between 2 coordinates which gives te distance between 2 points over the Great Circle.

# In[12]:

from math import radians, cos, sin, asin, sqrt
def haversine(a,b):
    # convert decimal degrees to radians 
    km_l = []
    for i in range(len(b)):
        lat1,lon1,lat2,lon2 = a[0],a[1],b[i][0],b[i][1]
        lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
        dlon = lon2 - lon1 
        dlat = lat2 - lat1 
        x = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
        c = 2 * asin(sqrt(x)) 
        km = 6367 * c
        km_l.append("{0:.2f}".format(km))
    km_l.sort()
    return km_l


# In[13]:

# Dummy GPS location of user
a = [20.564]
b=[78.5]
user = [20.564,78.5]
print(user)


# In[14]:

distance_actual = haversine(user,coord)

for o in range(len(distance_actual)):
    if (float(distance_actual[o])<500):
        f=1
        break
    else:
        f=0
if f==1:
    print("YOU ARE IN A DANGER AREA")
    print("You are in "+str(country[o+62100])+" country")
    print("Your nearby danger city is "+str(city[o+62100]))
else:
    print("YOU ARE SAFE")
    print(country)


# In[ ]:

import pickle


# In[15]:

mapbox_access_token = 'pk.eyJ1IjoiemVjdHJvc2FuIiwiYSI6ImNqN2QzamM2bjA1cXIzM3BkeXhlbnpjaHMifQ.h94ete_va3GUTxMFqKnLdg'


# In[17]:

data = Data([
    Scattermapbox(
        lat=lat_2014,
        lon=lon_2014,
        mode='markers',
        marker=Marker(
            color='rgb(255, 0, 0)',
            size=10
        )
        
    ),Scattermapbox(
        lat=lat_2015,
        lon=lon_2015,
        mode='markers',
        marker=Marker(
            color='rgb(0, 255, 0)',
            size=10
        )
        
    ),Scattermapbox(
        lat=lat_2016,
        lon=lon_2016,
        mode='markers',
        marker=Marker(
            color='rgb(255,255, 0)',
            size=10
        )
        
    ),Scattermapbox(
        lat=a,
        lon=b,
        mode='markers',
        marker=Marker(
            color='rgb(0, 0, 255)',
            size=10
        )
        
    )
])

layout = Layout(
    autosize=True,
    hovermode='closest',
    mapbox=dict(
        accesstoken=mapbox_access_token,
        bearing=0,
        center=dict(
            lat=a,
            lon=b
        ),
        pitch=0,
        zoom=2
    ),
)

fig = dict(data=data, layout=layout)
py.iplot(fig, filename='Terror Mapbox')

