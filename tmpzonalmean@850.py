# Zonal_Mean_Tmp@850
# 40N, 45N, 50N
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
midlat_1 = np.where(lat == 40)[0][0]
midlat_2 = np.where(lat == 45)[0][0]
midlat_3 = np.where(lat == 50)[0][0]

#establish 2Darrays for different latitudes' zonal all data (first dimension: , second dimension:)
tmp_midlat_1 = dat['t'][299:359, ilev, midlat_1, :]
tmp_midlat_2 = dat['t'][299:359, ilev, midlat_2, :]
tmp_midlat_3 = dat['t'][299:359, ilev, midlat_3, :]


#calculated zonal mean of each latitude, dimension = (60,)
zonal_mean_midlat_1 = np.sum(tmp_midlat_1, axis=1) / 1440.
zonal_mean_midlat_2 = np.sum(tmp_midlat_2, axis=1) / 1440.
zonal_mean_midlat_3 = np.sum(tmp_midlat_3, axis=1) / 1440.

#calculate climate value (2010-2016) of zonal means
MZM_1 = np.sum((np.sum(dat['t'][:, ilev, midlat_1, :], axis=1) / 1440.)) / 360.
MZM_2 = np.sum((np.sum(dat['t'][:, ilev, midlat_2, :], axis=1) / 1440.)) / 360.
MZM_3 = np.sum((np.sum(dat['t'][:, ilev, midlat_3, :], axis=1) / 1440.)) / 360.



#create
time_array = np.arange(10,25,0.25)


#set figure size
#plt.figure(figsize=(17, 26))


#split window
f, ax = plt.subplots(figsize=(11, 8.5))
axt = ax.twinx()

#plot 4 lines
ax.plot(time_array, zonal_mean_midlat_1 - MZM_1, color='mediumblue')
ax.plot(time_array, zonal_mean_midlat_2 - MZM_2, color='darkgreen')
ax.plot(time_array, zonal_mean_midlat_3 - MZM_3, color='#fabd00')


axt.plot(AO_date[0:10], AO_index[0:10], color='#d60a0a', ls='--')
axt.plot(AO_date[9:25], AO_index[9:25], color='#d60a0a')
axt.plot(AO_date[23::], AO_index[23::], color='#d60a0a', ls='--')
axt.plot(AO_date, np.zeros(31), color='pink')


ax.grid(color='gray',lw=.7)


#set ticks and limits
ax.set_xticks(np.arange(1, 33))
ax.set_xlim([10,25])
ax.set_ylim([-3,3])
ax.set_ylabel('Zonal Mean temperature Anomaly at 850 hPa (K)')
axt.set_ylim([-10,10])
axt.set_ylabel('Daily AO index')

#set legend
ax.legend(['40N', '45N', '50N'], loc='upper left')
axt.legend(['AO index'], loc='upper right')

#set title
ax.set_title('2016/01 Zonal Mean Tmp anomaly at 850 hPa')
#ax.set_title('2016/01 Zonal Mean Tmp anomaly of 50N at 850 hPa')

#save and show
#plt.savefig('ZMTA_50N_850hpa.png')
plt.savefig('ZMTA_50N_45N_40N_850hpa.png')
plt.tight_layout()
plt.show()
