import matplotlib.pyplot as plt
import numpy as np
import os

data_loc="/home/kabir/Blender/2x2_diff_files/2x2_diff_files/mcell/Average/"

plt.close('all')

f,plots=plt.subplots(8,sharex=True)

for (pl,file) in zip(plots,os.listdir(data_loc)):
    data=np.loadtxt(os.path.join(data_loc,file))
    pl.set_title(file)
    pl.plot(data.T[0], data.T[1])

f.subplots_adjust(hspace=0.3)
plt.show()
