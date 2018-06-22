#$1=model number and $2=number of seeds
model=100
num_of_sim=1
model=$1
num_of_sim=$2
seq "$num_of_sim"|parallel mcell /home/kabir/project/mcell"$model"/main.mdl -seed {}
echo "Averaging"
python avg.py mcell"$model"
echo "Plotting"
python plotter.py mcell"$model"
