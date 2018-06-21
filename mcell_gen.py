import box_maker as bm
import os
import pkl

model_folder="/home/kabir/project/mcell100/"
geom_desc_loc="/home/kabir/project/mcell100.txt"
big_box_size=[40,20,10]
pklfile=os.path.join(model_folder,"all_boxes.pkl")
stand_mdls="/home/kabir/project/stand_mdls/"

bm.main(geom_desc_loc,pklfile,big_box_size)

#bm.BOXES()

#make init.mdl
f=open('')
