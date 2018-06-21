import matplotlib.pyplot as plt
import numpy as np
import os
import sys



data_loc=os.getcwd()+"/"+sys.argv[1]+"/Average/"

plt.close('all')

f,plots=plt.subplots(8,sharex=True)

for (pl,file) in zip(plots,os.listdir(data_loc)):
    data=np.loadtxt(os.path.join(data_loc,file))
    pl.set_title(file)
    pl.plot(data.T[0], data.T[1])

f.subplots_adjust(hspace=0.3)
plt.show()
