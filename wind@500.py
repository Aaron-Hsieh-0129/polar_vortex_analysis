# wind@500
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
ilev = np.where(lev==500)[0][0]
lon2, lat2 = np.meshgrid(lon, lat)
for i in range(60):
  uw = dat['u'][300+i, ilev]
  vw = dat['v'][300+i, ilev]
  wm = (uw ** 2 + vw ** 2) ** (1 / 2)
  wmm = np.where(wm < 63.9, wm, 63.9)

    #wind = dat['wm'][300+i, ilev[0][3], 0:721, :]
  plt.figure(figsize = (13, 8.5))
  m = Basemap(projection='ortho', lon_0=90, lat_0=50)
  cx, cy = m(lon2, lat2)
  m.drawcoastlines(color='white')

    #t_good=np.where(tmp>243.15, tmp, 243.15)
    #t_good2=np.where(tmp<311.15, t_good, 311.15)

  tm = m.contourf(cx, cy, wmm, cmap = cm.RdYlBu_r, levels = np.arange(0, 64, 0.1))
    # levels = np.arange(-43, 27, 0.1)
  m.colorbar(tm)

  day=10+i//4
  hour=6*(i%4)
  hour_good=('%02.2d' %(hour))

  plt.title('Wind velocity at 500 hPa 2016/01/'+str(day)+'_'+str(hour_good)+'Z', fontsize=25)
  plt.savefig('Wind velocity_201601'+str(day)+'_'+str(hour_good)+'Z.png')
  plt.tight_layout()
  plt.show()

