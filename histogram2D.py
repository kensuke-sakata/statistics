#!/usr/bin/env python
# coding: utf-8

# In[1]:

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.cm as cm
plt.rcParams['font.size'] = 20 # in graph

# read dat file
df = pd.read_table('RotorTissue-LFDFE.dat')
df

# In[2]:

# x
x_name = 'FD'
x_data = df[x_name]
x_data

# In[3]:

# y
y_name = 'FE'
y_data = df[y_name]
y_data

# In[4]:

# histogram-A
fig = plt.figure()
ax = fig.add_subplot(111)

g = ax.hist2d(x_data, y_data, bins = 60, cmap = cm.jet)
ax.set_xlabel(x_name)
ax.set_ylabel(y_name)
fig.colorbar(g[3], ax = ax)
plt.show()

# In[5]:

# histogram-B
sns.jointplot(x = x_data, y = y_data, kind = 'hex', color = 'magenta')
plt.xlabel(x_name)
plt.ylabel(y_name)
plt.grid()
plt.show()

# In[ ]:
