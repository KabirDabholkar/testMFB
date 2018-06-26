from multiprocessing import Pool
import numpy as np
import os, time
import sys
import pickle as pkl
import init

N_avo=6.0221409e23

#set mcell directory
dir=init.projDir+sys.argv[1]+"/"

#averaged data
avg_path=os.path.join(dir,"Average")
if not os.path.exists(avg_path):
    os.makedirs(avg_path)

    
#reaction data
rxn_path=os.path.join(dir,"react_data")
seed_folders=os.listdir(rxn_path)
file_names=os.listdir(os.path.join(rxn_path,seed_folders[0]))

#box data
f=open(os.path.join(dir,"all_boxes.pkl"),'r')
boxes=pkl.load(f)

def array_to_txtfile(arr,file):
    for line in arr:
        file.write(str(line[0])+" "+str(line[1])+" "+str(line[2])+"\n")

#return volume of box by its .dat file name in micrometer cube 
def get_volume(dat_file_name):
    name=dat_file_name[:-4]
    box=boxes[name]
    vol=box[3]*box[4]*box[5]
    return vol

def get_data(box_name):
    data=[]
    for seed_folder in seed_folders:
        folder_path=os.path.join(rxn_path,seed_folder)
        data.append(np.loadtxt(os.path.join(folder_path,box_name)).T[1])
    return np.array(data)

#data_shape=np.loadtxt(os.path.join(os.path.join(rxn_path,seed_folders[0]),file_names[0])).shape
#print data_shape
#start=time.time()
times=np.loadtxt(os.path.join(os.path.join(rxn_path,seed_folders[0]),file_names[0])).T[0]
def evaluate(file_name):
    data=get_data(file_name)
    avg=np.average(data,axis=0)
    std=np.std(data,axis=0)
    #concentration in millimoles
    avg*=1e15/N_avo/get_volume(file_name)
    std*=1e15/N_avo/get_volume(file_name)
    f=open(os.path.join(avg_path,file_name),'w')
    array_to_txtfile(np.stack([times,avg,std],axis=-1),f)
    f.close()

p = Pool(processes=16)
p.map(evaluate, file_names)

#end=time.time()
#print (end-start)


