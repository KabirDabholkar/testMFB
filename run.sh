seq 16|parallel mcell /home/kabir/project/mcell100/main.mdl -seed {}
echo "Averaging"
python avg.py mcell100
echo "Plotting"
python plotter.py mcell100
