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


#uw = dat['ugrdprs'][0, ilev, :, :]
#vw = dat['vgrdprs'][0, ilev, :, :]
#wm = (uw ** 2 + vw ** 2) ** (1/2)

for i in range(60):
    tmp = dat['t'][300+i, ilev[0][3], 0:721, :]
    plt.figure(figsize = (13, 8.5))
    m = Basemap(projection='ortho', lon_0=120,lat_0=50)
    cx, cy = m(lon2, lat2)
    m.drawcoastlines(color='white')

    t_good=np.where(tmp>243.15, tmp, 243.15)
    t_good2=np.where(tmp<311.15, t_good, 311.15)

    tm = m.contourf(cx, cy, t_good2-273.15, cmap = cm.RdBu_r, levels = np.arange(-30, 33, 0.1))
    # levels = np.arange(-43, 27, 0.1)
    m.colorbar(tm)

    day=10+i//4
    hour=6*(i%4)
    hour_good=('%02.2d' %(hour))

    plt.title('Tmp at 850 hPa 2016/01/'+str(day)+'_'+str(hour_good)+'Z', fontsize=25)
    plt.savefig('Tmp_201601'+str(day)+'_'+str(hour_good)+'Z.png')
    plt.tight_layout()
    plt.show()