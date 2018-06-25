import matplotlib.pyplot as plt
import numpy as np
import os
import sys
import init


mcell_loc=init.projDir+"mcell100/Average/b1_0_0.dat"
ode_loc=init.projDir+"ode/data100/trial/1-0-0.txt"

plt.close('all')
mcell_data=np.loadtxt(mcell_loc)
ode_data=np.loadtxt(ode_loc)
np.delete(ode_data,0)
#print ode_data
plt.plot(mcell_data.T[0], mcell_data.T[1],'r-', ode_data.T[0], ode_data.T[1],'b-')
plt.fill_between(mcell_data.T[0], mcell_data.T[1]-mcell_data.T[2], mcell_data.T[1]+mcell_data.T[2], facecolor='yellow', alpha=0.5,label='1 sigma range')
"""
f,plots=plt.subplots(8,sharex=True)
data=np.loadtxt(mcell_data)
data=np.loadtxt(mcell_data)
pl.set_title('0-0-0')
pl.plot(data.T[0], data.T[1])

f.subplots_adjust(hspace=0.3)
"""
plt.show()
