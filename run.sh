seq 16|parallel mcell /home/kabir/project/mcell50/main.mdl -seed {}
echo "Averaging"
python avg.py mcell50
echo "Plotting"
python plotter.py mcell50
