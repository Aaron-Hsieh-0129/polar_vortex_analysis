import matplotlib.pyplot as plt
import numpy as np
import netCDF4 as nc
import matplotlib.cm as cm

import os
os.environ['PROJ_LIB']='/Users/wei/anaconda/anaconda3/envs/python_anaconda/share/proj'
from mpl_toolkits.basemap import Basemap

dat = nc.Dataset('file.nc')
lon = dat['longitude'][:]
lat = dat['latitude'][:]
lev = dat['level'][:]
lon2, lat2 = np.meshgrid(lon, lat)
ilev = np.where(lev==850)[0][0]
tmp = np.zeros([360, 721, 1440])
tmpan = np.zeros([60, 721, 1440])

for i in range(360):
    tmp[i] = dat['t'][i, ilev]
tmpa = sum(tmp)/360

for i in range(60):
    tmpan[i] = tmp[300+i] - tmpa
    plt.figure(figsize = (13, 8.5))
    plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1)
    m = Basemap(projection='cyl', lat_0 = 0, lon_0 = 180)
    cx, cy = m(lon2, lat2)
    m.drawcoastlines(color='white')

    parallels = np.arange(-90., 90.1, 30.)
    m.drawparallels(parallels, labels=[1, 1, 0, 0], fontsize=10)

    meridians = np.arange(-180., 180., 30.)

    m.drawmeridians(meridians, labels=[0, 0, 0, 1], fontsize=10)

    t_good=np.where(tmpan[i]<=12.4, tmpan[i], 12.4)
    t_good2=np.where(t_good>=-12.5, t_good, -12.5)

    tm = m.contourf(cx, cy, t_good2, cmap = cm.RdBu_r, levels = np.arange(-12.5, 12.6, 0.1))
    m.colorbar(tm, location = 'bottom', pad = 0.5)

    day=10+i//4
    hour=6*(i%4)
    hour_good=('%02.2d' %(hour))

    plt.title('Anomaly Temperature at 850 hPa 2016/01/' + str(day) + '_' + str(hour_good) + 'Z', fontsize=20)
    plt.tight_layout()
    plt.savefig('Anomaly temperature at 850 hPa' + str(day) + '_' + str(hour_good) + 'Z.png')
    plt.show()