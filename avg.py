import numpy as np
import os

dir="/home/kabir/Blender/2x2_diff_files/2x2_diff_files/mcell/react_data/"
seed_folders=os.listdir(dir)

avg_path=os.path.join("/home/kabir/Blender/2x2_diff_files/2x2_diff_files/mcell/","Average")
if not os.path.exists(avg_path):
    os.makedirs(avg_path)

file_names=os.listdir(os.path.join(dir,seed_folders[0]))


def array_to_txtfile(arr,file):
    for line in arr:
        file.write(str(line[0])+" "+str(line[1])+"\n")

data_shape=np.loadtxt(os.path.join(os.path.join(dir,seed_folders[0]),file_names[0])).shape
print data_shape

for file_name in file_names:
    avg=np.zeros(data_shape)
    for seed_folder in seed_folders:
        folder_path=os.path.join(dir,seed_folder)
        dat=np.loadtxt(os.path.join(folder_path,file_name))
        avg+=dat
    avg/=len(seed_folders)
    f=open(os.path.join(avg_path,file_name),'w')
    array_to_txtfile(avg,f)
    f.close()
