import matplotlib.pyplot as plt
import numpy as np
import os
import sys
import init

#arguments model_number, box_name eg. $ python plotter2.py 100 0-0-0

mcell_loc=init.projDir+"mcell"+str(sys.argv[1])+"/Average/b"+str(sys.argv[2]).replace('-','_')+".dat"
ode_loc=init.projDir+"ode/data"+str(sys.argv[1])+"/trial/"+str(sys.argv[2])+".txt"

plt.close('all')

mcell_data=np.loadtxt(mcell_loc)
ode_data=np.loadtxt(ode_loc)
#removing the column titles
np.delete(ode_data,0) 

plt.plot(mcell_data.T[0], mcell_data.T[1],'r-', ode_data.T[0], ode_data.T[1],'b-')
plt.fill_between(mcell_data.T[0], mcell_data.T[1]-mcell_data.T[2], mcell_data.T[1]+mcell_data.T[2], facecolor='yellow', alpha=0.5,label='1 sigma range')

plt.show()
