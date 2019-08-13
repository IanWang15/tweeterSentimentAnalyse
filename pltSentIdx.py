#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 23:07:52 2019

@author: yiwang
"""

import matplotlib as mpl
mpl.use('Agg')
import time, calendar, datetime
import numpy as np
from mpl_toolkits.basemap import Basemap,cm
from matplotlib.colors import LinearSegmentedColormap
import matplotlib.pyplot as plt
import urllib, os

filename = 'sentimentOutput.txt'

data = np.loadtxt(filename)
print 'lenth is ', len(data)

lats    = np.zeros(len(data))
lons    = np.zeros(len(data))
sentIdx = np.zeros(len(data))
for j in range(0,len(data)):
    lats[j]    = float(data[j,0]) # latitude
    lons[j]    = float(data[j,1]) # longitude
    sentIdx[j] = float(data[j,2]) # sentiment scores component 1

print 'start plotting ...'

# create polar stereographic Basemap instance.
m = Basemap(projection = 'stere', lon_0 = -95, lat_0 = 30., lat_ts = 30.,\
            llcrnrlat = 29.26, urcrnrlat = 30.26,\
            llcrnrlon = -95.86, urcrnrlon = -94.86,\
            rsphere = 6371200., area_thresh = 10000)

lats = map(float,lats)
lons = map(float,lons)
RougValue = map(int,RougValue)

x, y = m(lons,lats)

# draw coastlines, state and country boundaries, edge of map.
m.drawcoastlines()
#m.drawstates()
m.drawcountries()
# draw parallels.
parallels = np.arange(-90.,90,0.1)
m.drawparallels(parallels,labels=[1,0,0,0],fontsize=10)
# draw meridians
meridians = np.arange(0.,360.,0.1)
m.drawmeridians(meridians,labels=[0,0,0,1],fontsize=10)
# draw filled contours.
cs=m.scatter(x, y, c = sentIdx, s = 0.05, lw=0, cmap = plt.cm.get_cmap("jet",lut=8))#cmap = cm.GMT_drywet._resample(13),marker='h',cmap=plt.cm.jet('Spectral_r',13),s=2.5,lw=0)#cmap=cm.s3pcpn)

#plt.title('Sentiment Index',fontsize=18)

cbar=plt.colorbar(cs, orientation='vertical')#, shrink=0.6)#,pad=0.12,aspect=50)
cbar.ax.tick_params(labelsize=8)
cbar.set_label(label='Sentiment Index',size=18)

pngname = "./sentimentIdx"+".png"
print "save ", pngname
plt.savefig(pngname, dpi=200, facecolor='w', edgecolor='w',
    orientation='portrait', papertype=None, format=None,
    transparent=False, bbox_inches='tight', pad_inches=0.1)
plt.show()

print "Computation is done"

