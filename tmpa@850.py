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
ilev = np.where(dat['level'])
tmp = np.zeros([90, 721, 1440])


for i in range(90):
    tmp[i] = dat['t'][3+4*i, ilev[0][3], 0:721, :]
tmpa = sum(tmp)/90
plt.figure(figsize = (13, 8.5))
m = Basemap(projection='ortho', lon_0=120,lat_0=50)
cx, cy = m(lon2, lat2)
m.drawcoastlines(color='white')

t_good=np.where(tmpa>243.15, tmpa, 243.15)
t_good2=np.where(tmpa<311.15, t_good, 311.15)

tm = m.contourf(cx, cy, t_good2-273.15, cmap = cm.RdBu_r, levels = np.arange(-27, 38, 0.1))
# levels = np.arange(-43, 27, 0.1)
m.colorbar(tm)

#day=10+i//4
#hour=6*(i%4)
#hour_good=('%02.2d' %(hour))

plt.title('Average tmp at 850 hPa from 2011 to 2016', fontsize=25)
plt.savefig('Average tmp at 850 hPa from 2011 to 2016.png')
plt.tight_layout()
plt.show()

print(tmp[198][460])
print(tmpa[260][484])
print(tmpa[234][482])
