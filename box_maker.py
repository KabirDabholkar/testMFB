import numpy as np
import pickle as pkl

#geometry_file_location="/home/kabir/Blender/scripts/mcell100.txt"
#big_box_size=[40,20,10]
#pklfilename="all_boxes_100.pkl"

"""
calcium_diff_const
sim_time_step
data_time_step
calium_constant
"""

#delta space between surfaces
delta=1e-3
#default unit in micrometeres
unit=50e-3
#big dict of all the boxes
BOXES={}

def make_box ( name, x, y, z, sx, sy, sz ):
    box = {
      'element_connections' : [
        [3, 0, 1],
        [7, 2, 3],
        [5, 6, 7],
        [1, 4, 5],
        [2, 4, 0],
        [7, 1, 5],
        [3, 2, 0],
        [7, 6, 2],
        [5, 4, 6],
        [1, 0, 4],
        [2, 6, 4],
        [7, 3, 1]
      ],
      'location' : [x, y, z],
      'name' : name,
      'vertex_list' : [
        [0, 0, 0],
        [0, 0, sz],
        [0, sy, 0],
        [0,  sy,  sz],
        [ sx, 0, 0],
        [ sx, 0,  sz],
        [ sx,  sy, 0],
        [ sx,  sy,  sz]
      ]
    }
    return box


def gen_boxes(line):
    xyz=line[1:-2].split(",")
    box_details=[]
    all_axial_info=[]
    for axis in xyz:
        axial_info=[int(i) for i in axis.split(":")]
        start_coord,end_coord=axial_info[0],axial_info[1]
        res=1
        if len(axial_info)>2:
            res=axial_info[2]
        all_axial_info.append([start_coord,end_coord,res])
    ranges=[range(all_axial_info[i][0],all_axial_info[i][1],all_axial_info[i][2]) for i in [0,1,2]]
    sizes=[all_axial_info[i][2] for i in [0,1,2]]
    for x in ranges[0]:
        for y in ranges[1]:
            for z in ranges[2]:
                box_details.append(np.array([x,y,z,sizes[0]-delta,sizes[1]-delta,sizes[2]-delta]))
    #create big box
    return box_details

#returns a list lines of box description after reading and removing the unit= line
def read_desc(geometry_file_location):
    file=open(geometry_file_location,'r')
    lines=file.readlines()
    for line in lines:
        if "unit" in line:
            unit=float(line[5:])*1e-3
            lines.pop()
    file.close()
    return lines


#creates all boxes including big box
def create_all_boxes(lines,big_box_size):
    for line in lines:
    	boxes=gen_boxes(line)
        for box in boxes:
            box_name="b"+str(int(box[0]))+"_"+str(int(box[1]))+"_"+str(int(box[2]))
            box*=unit
	    BOXES[box_name]=box
    big_box=np.array([-delta,-delta,-delta,big_box_size[0]+delta,big_box_size[1]+delta,big_box_size[2]+delta])
    big_box*=unit
    BOXES['big_box']=big_box

#dumps box datas into a file
def dump_pkl(pklfilename):
    DATA_FILE=open(pklfilename,'wb')
    pkl.dump(BOXES,DATA_FILE)
    DATA_FILE.close()

def main(geom_desc_loc,pkl_file,big_box_size):
    create_all_boxes(read_desc(geom_desc_loc),big_box_size)
    dump_pkl(pkl_file)
