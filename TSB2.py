# Tmp@850
# Taipei(121, 25)
# Shanghai(120.5, 31.5)
# Beijing(115, 40.5)
import matplotlib.pyplot as plt
import numpy as np
import netCDF4 as nc
import matplotlib.cm as cm

import os
os.environ['PROJ_LIB']='/Users/wei/anaconda/anaconda3/envs/python_anaconda/share/proj'
from mpl_toolkits.basemap import Basemap

#read data from .nc
dat = nc.Dataset('file.nc')
lon = dat['longitude'][:]
lat = dat['latitude'][:]
lev = dat['level'][:]
time = dat['time'][:]

#read AO index from .txt
fo = open('AO_index.txt', 'r')
AO_date, AO_index = np.loadtxt('AO_index.txt', usecols=(2, 3), unpack=True)


#set region and levels
ilev = np.where(lev == 850)[0][0]
Harbin_lat = np.where(lat == 45.5)[0][0]
Harlin_lon = np.where(lon == 126.0)[0][0]
taipei_lat = np.where(lat == 25)[0][0]
taipei_lon = np.where(lon == 121)[0][0]
Qingdao_lat = np.where(lat == 36.5)[0][0]
Qingdao_lon = np.where(lon == 120.0)[0][0]

#establish arrays for x-axis and y-axis
tmp_Harbin = dat['t'][299:359, ilev, Harbin_lat, Harlin_lon]
tmp_Qingdao = dat['t'][299:359, ilev, Qingdao_lat, Qingdao_lon]
tmp_taipei = dat['t'][299:359, ilev, taipei_lat, taipei_lon]
time_array = np.arange(10,25,0.25)


#set figure size
plt.figure(figsize=(17, 26))


#split window
f, ax = plt.subplots(figsize=(11, 8.5))
axt = ax.twinx()

#plot 4 lines
ax.plot(time_array, tmp_Harbin-254.200, color='mediumblue')
ax.plot(time_array, tmp_Qingdao-265.001, color='darkgreen')
ax.plot(time_array, tmp_taipei-280.060, color='#fabd00')


axt.plot(AO_date[0:10], AO_index[0:10], color='#d60a0a', ls='--')
axt.plot(AO_date[9:25], AO_index[9:25], color='#d60a0a')
axt.plot(AO_date[23::], AO_index[23::], color='#d60a0a', ls='--')
axt.plot(AO_date, np.zeros(31), color='pink')

axt.grid(color='gray',lw=.7)
#ax.grid(color='gray',lw=.7)


#set ticks and limits
ax.set_xticks(np.arange(1, 33))
ax.set_xlim([1,31])
ax.set_ylim([-20,20])
ax.set_ylabel('temperature at 850 hPa (K)')
axt.set_ylim([-10,10])
axt.set_ylabel('Daily AO index')

#set legend
ax.legend(['Harbin', 'Qingdao', 'Taipei'])
axt.legend(['AO index'], loc='upper left')

#set title
ax.set_title('2016/01 Tmp at 850 hPa')

#save and show
plt.savefig('Anomaly_Tmp_201601_HQT')
plt.tight_layout()
plt.show()