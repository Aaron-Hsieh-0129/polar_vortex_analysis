# GP@500
import matplotlib.pyplot as plt
import numpy as np
import netCDF4 as nc

import os
os.environ['PROJ_LIB']='/Users/wei/anaconda/anaconda3/envs/python_anaconda/share/proj'
from mpl_toolkits.basemap import Basemap
import matplotlib.cm as cm

dat = nc.Dataset('file.nc')
lon = dat['longitude'][:]
lat = dat['latitude'][:]
lev = dat['level'][:]
ilev = np.where(lev==500)[0][0]
z = dat['z'][0, ilev]

for i in range(60):
  z1 = dat['z'][300+i, ilev]
  lon2, lat2 = np.meshgrid(lon, lat)
#tp = dat['tmpprs'][0, 13, :, :]
#o3m = np.average(o3[:, :, :],axis = 0)



  plt.figure(figsize = (13, 9.5))

  m = Basemap(projection='ortho', lon_0=120, lat_0=90)

#m = Basemap(projection = 'npstere',boundinglat = 0, lon_0 = 0)

  m.drawcoastlines(color = 'black')
  cx, cy = m(lon2, lat2)

#tm = m.contourf(cx,cy,tp,cmap = 'jet', levels = np.arange(215, 275, 0.1))
#tm = m.pcolormesh(cx,cy,tp,cmap = cm.rainbow,shading = 'gouraud')
#m.colorbar(tm)

  z_good = np.where(z1 > 47400, z1, 47400)

#w = m.pcolormesh(cx, cy, z, cmap = 'jet', shading = 'gouraud')
  #w = m.contourf(cx, cy, t_good, cmap = cm.Purples_r, levels=np.arange(50700, 58000, 350))
  w = m.contourf(cx, cy, z_good, cmap=cm.RdYlBu_r, levels = np.arange(47400, 60000, 350))
  #w = m.contourf(cx, cy, z1, cmap=cm.bone)
 # levels = np.arange(46500, 58500, 350)
  m.colorbar(w)

  day = 10 + i // 4
  hour = 6 * (i % 4)
  hour_good = ('%02.2d' % (hour))

  plt.title('Geo-potential Height at 500 hPa 2016/01/' + str(day) + '_' + str(hour_good) + 'Z', fontsize=20)
  plt.tight_layout()
  plt.savefig('Geo-potential_Height_201601'+str(day)+'_'+str(hour_good)+'Z.png')
  plt.show()