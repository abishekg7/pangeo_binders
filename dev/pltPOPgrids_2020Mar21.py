#!/usr/bin/env python
# coding: utf-8

# In[1]:


#get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
import pop_tools # https://github.com/NCAR/pop-tools
import util
import cartopy
import xarray as xr
import numpy as np


# In[2]:


ds = pop_tools.get_grid('POP_tx0.1v3')
ds


# In[3]:


dsp = util.pop_add_cyclic(ds)
dsp


# In[4]:


infile = '../raw_data/select_hybrid_v5_rel04_BC5_ne120_t12_pop62_diag.02.pop.h.nday1.0087-03-01_ncksTAUXTAUYSSHDXUDYUTAREAUAREA_DL_2020Mar03.nc'
ds1 = xr.open_dataset(infile,chunks={'time':1})
ds1


# In[5]:


#dsp = util.pop_add_cyclic(ds1)
#dsp


# In[6]:


ds.TLONG.where(ds.KMT > 0).plot()


# In[7]:


dsp.TLONG.where(dsp.KMT > 0).plot()


# In[8]:


# proj = cartopy.crs.Mollweide(central_longitude=180)
# pc = cartopy.crs.PlateCarree()
# fig = plt.figure()
# ax = fig.add_subplot(111,projection=pc)
# dsp.TLONG.where(dsp.KMT > 0).plot(transform=pc)
# plt.savefig('POPgrids_2020Mar20.png')
# ds2.cprat.sel(time='2010-1-1').plot(transform=pc) 
# xarray plot directly with matplotlib, transform=pc is consistent with lat and lon in ds2.cprat


# In[9]:


lon = dsp.TLONG[0:-1:1,0:-1:1]
lat = dsp.TLAT[0:-1:1,0:-1:1]
# Tarea = dsp.TAREA[1:-1:10,1:-1:10]
# KMT = dsp.KMT[1:-1:3,1:-1:3]
ssh = ds1.SSH[10,0:-1:1,0:-1:1]/100
# taux = ds1.TAUX[10,1:-1:5,1:-1:5]
print(lon.shape, lat.shape)
print(ssh.shape)


# In[10]:


# taux[np.where(ds1.KMT<0)]=0


# In[20]:


proj = cartopy.crs.Mollweide(central_longitude=270)
pc = cartopy.crs.PlateCarree()

fig = plt.figure(figsize=(10, 6))

ax = fig.add_subplot(111,projection=pc)
subplt1 = ax.pcolormesh(lon,lat,ssh,vmin=-0.5,vmax=0.5,cmap='bwr',transform=pc)
gl = ax.gridlines(linewidth=0.2, color='gray', alpha=0.5, linestyle='-')
ax.set_xticks([-180, -120, -60, 0, 60, 120, 180], crs=pc)
ax.set_yticks([-90, -45, 0, 45, 90],crs=pc)
cb = plt.colorbar(subplt1,shrink=0.5)
# cb.set_label('T [C]') # option K
# cb.set_label('T [$\degree$C]')
cb.set_label('[m]') # \xb0, add degree symbol

# set title with datetime
#time = np.atleast_1d(data.time.values)[0] #  np.atleast_1d(data.time.values) output array, index into it
ax.set_title('SSH',fontsize=16)

plt.savefig('POPoriginalGridsSSH_2020Apr06.png')


# In[ ]:




