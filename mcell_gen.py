import box_maker as bm
import os
import pickle as pkl
import numpy as np
import init

model_folder=init.projDir+"mcell100/"
geom_desc_loc=init.projDir+"mcell100.txt"
big_box_size=[24,24,14]
pklfile=os.path.join(model_folder,"all_boxes.pkl")
stand_mdls="~/project/stand_mdls/"

sim_time_step=1e-6
data_time_step=1e-5
init_conc=1e-6

bm.main(geom_desc_loc,pklfile,big_box_size)



#initialization.mdl
file_string='''SURFACE_GRID_DENSITY = 10000
ACCURATE_3D_REACTIONS = TRUE
CENTER_MOLECULES_ON_GRID = FALSE
MICROSCOPIC_REVERSIBILITY = OFF

NOTIFICATIONS
{
   PROBABILITY_REPORT = ON
   DIFFUSION_CONSTANT_REPORT = BRIEF
   FILE_OUTPUT_REPORT = OFF
   FINAL_SUMMARY = ON
   ITERATION_REPORT = ON
   PARTITION_LOCATION_REPORT = OFF
   VARYING_PROBABILITY_REPORT = ON
   PROGRESS_REPORT = ON
   RELEASE_EVENT_REPORT = ON
   MOLECULE_COLLISION_REPORT = OFF
}

WARNINGS
{
   DEGENERATE_POLYGONS = WARNING
   NEGATIVE_DIFFUSION_CONSTANT = WARNING
   MISSING_SURFACE_ORIENTATION = ERROR
   NEGATIVE_REACTION_RATE = WARNING
   USELESS_VOLUME_ORIENTATION = WARNING
   HIGH_REACTION_PROBABILITY = IGNORED
   LIFETIME_TOO_SHORT = WARNING
   LIFETIME_THRESHOLD = 50
   MISSED_REACTIONS = WARNING
   MISSED_REACTION_THRESHOLD = 0.00100000004749745
}
'''
with open(os.path.join(model_folder,'initialization.mdl'), "w") as out_file:
    for line in file_string:
        out_file.write(line)

#main.mdl
file_string=['''ITERATIONS = 1000
TIME_STEP = '''+str(sim_time_step)+'''
VACANCY_SEARCH_DISTANCE = 10

INCLUDE_FILE = "initialization.mdl"

INCLUDE_FILE = "molecules.mdl"

INCLUDE_FILE = "surface_classes.mdl"

INCLUDE_FILE = "geometry.mdl"

INCLUDE_FILE = "mod_surf_regions.mdl"

INSTANTIATE Scene OBJECT
{
''','''
  release RELEASE_SITE
  {
   SHAPE = Scene.b0_0_0
   MOLECULE = Ca
   CONCENTRATION = '''+str(init_conc)+'''
   RELEASE_PROBABILITY = 1
  }
}

sprintf(seed,"%05g",SEED)

INCLUDE_FILE = "viz_output.mdl"

INCLUDE_FILE = "rxn_output.mdl"
''']

with open(os.path.join(model_folder,'main.mdl'), "w") as out_file:
    for line in file_string[0]:
        out_file.write(line)
    for box in bm.BOXES.keys():
             out_file.write("  "+box+" OBJECT "+box+" {}\n")
    for line in file_string[1]:
        out_file.write(line)


#molecules.mdl
file_string='''DEFINE_MOLECULES
{
  Ca   {DIFFUSION_CONSTANT_3D = 2.2e-6}
  calB {DIFFUSION_CONSTANT_3D = 0.28e-6}
}'''
with open(os.path.join(model_folder,'molecules.mdl'), "w") as out_file:
    for line in file_string:
        out_file.write(line)

#mod_surf_regions.mdl
with open(os.path.join(model_folder,'mod_surf_regions.mdl'), "w") as out_file:
    out_file.write("MODIFY_SURFACE_REGIONS\n{\n")
    for box in bm.BOXES.keys():
        if box=="big_box":
            out_file.write("  "+box+"[ALL]\n  {\n    SURFACE_CLASS = refl\n  }\n")
        else:
            out_file.write("  "+box+"[ALL]\n  {\n    SURFACE_CLASS = transp\n  }\n")
    out_file.write("}")

#viz_output.mdl
file_string='''VIZ_OUTPUT
{
  MODE = CELLBLENDER
  FILENAME = "'''+model_folder+'''viz_data/seed_" & seed & "/Scene"
  MOLECULES
  {
    NAME_LIST {ALL_MOLECULES}
    ITERATION_NUMBERS {ALL_DATA @ ALL_ITERATIONS}
  }
}'''

with open(os.path.join(model_folder,'viz_output.mdl'), "w") as out_file:
    for line in file_string:
        out_file.write(line)


#surface_classes.mdl
file_string='''DEFINE_SURFACE_CLASSES
{
  transp
  {
    TRANSPARENT = ALL_MOLECULES;
  }
  refl
  {
    REFLECTIVE = ALL_MOLECULES;
  }
}'''
with open(os.path.join(model_folder,'surface_classes.mdl'), "w") as out_file:
    for line in file_string:
        out_file.write(line)

#geometry.mdl
def vertices(box):
    vert=[]
    vert.append("    [ "+str(box[0])+", "+str(box[1])+", "+str(box[2])+" ]\n")
    vert.append("    [ "+str(box[0])+", "+str(box[1])+", "+str(box[2]+box[5])+" ]\n")
    vert.append("    [ "+str(box[0])+", "+str(box[1]+box[4])+", "+str(box[2])+" ]\n")
    vert.append("    [ "+str(box[0])+", "+str(box[1]+box[4])+", "+str(box[2]+box[5])+" ]\n")
    vert.append("    [ "+str(box[0]+box[3])+", "+str(box[1])+", "+str(box[2])+" ]\n")
    vert.append("    [ "+str(box[0]+box[3])+", "+str(box[1])+", "+str(box[2]+box[5])+" ]\n")
    vert.append("    [ "+str(box[0]+box[3])+", "+str(box[1]+box[4])+", "+str(box[2])+" ]\n")
    vert.append("    [ "+str(box[0]+box[3])+", "+str(box[1]+box[4])+", "+str(box[2]+box[5])+" ]\n")
    return vert

file_string='''  ELEMENT_CONNECTIONS
  {
    [ 3, 0, 1 ]
    [ 7, 2, 3 ]
    [ 5, 6, 7 ]
    [ 1, 4, 5 ]
    [ 2, 4, 0 ]
    [ 7, 1, 5 ]
    [ 3, 2, 0 ]
    [ 7, 6, 2 ]
    [ 5, 4, 6 ]
    [ 1, 0, 4 ]
    [ 2, 6, 4 ]
    [ 7, 3, 1 ]
  }
}\n\n'''

with open(os.path.join(model_folder,'geometry.mdl'), "w") as out_file:
    for box in bm.BOXES.keys():
        out_file.write(box+" POLYGON_LIST\n{\n  VERTEX_LIST\n  {\n")
        for line in vertices(bm.BOXES[box]):
            out_file.write(line)
        out_file.write("  }\n")
        out_file.write(file_string)

#rxn_output.mdl
with open(os.path.join(model_folder,'rxn_output.mdl'), "w") as out_file:
    out_file.write("REACTION_DATA_OUTPUT\n{\n  STEP="+str(data_time_step)+"\n")
    for box in bm.BOXES.keys():
        out_file.write('  {COUNT[Ca,Scene.'+box+']} =>  "'+model_folder+'react_data/seed_" & seed & "/'+box+'.dat"\n')
    out_file.write("}")

        
        


        
