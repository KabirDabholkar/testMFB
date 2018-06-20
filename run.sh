seq 16|parallel mcell /home/kabir/Blender/2x2_diff_files/2x2_diff_files/mcell/Scene.main.mdl -seed {}
python avg.py
python plotter.py
