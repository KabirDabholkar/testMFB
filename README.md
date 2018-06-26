Hi! Here is a list of the codes that I have written.

##init.py
Set the directory location for the project.

##Box Description to MCell model. 
`box_maker.py` contains functions to generate a dict() called BOXES which uses `'b0_0_0'` format as the key.
The `box_maker.main(geom_desc_loc,pkl_file,big_box_size)` function reads the complete box description(.txt file), generates the dict() and dumps it into the a .pkl file.
 ###Here's how to use box_maker 
 ```shell
$ python
```
```python
>>> import box_maker as bm
>>> bm.main('mcell8.txt','./mcell8/all_boxes.pkl',[2,2,2])
>>> bm.BOXES['b0_0_0']
array([0.     , 0.     , 0.     , 0.04995, 0.04995, 0.04995])
```
The elements of BOXES are numpy arrays containing corner-coordinates and dimensions of the box `[x y z sx sy sz]` in micrometers.   

`mcell_gen.py` imports `box_maker.py` and writes all the `.mdl` files for the MCell model using the given box geometry. By default it uses '`b0_0_0'` as the release site. At the top of `mcell_gen.py` you need to specify a couple of details as per your requirements of the MCell model.
The `all_boxes.pkl` is stored in the corresponding model folder.

##run.sh
This short bash script runs the mcell model for a number of diffent seeds.
It takes `8` as in mcell8 as the first argument and `128` as in 128 seeds as the second argument.
###Here's how to use run.sh
```shell
$ ./run.sh 8 128
```

At this point all the reaction data is stored `/react_data/` in the corresponding seed folders.

##avg3.py
This is the fastest code to obtain average and standard deviation of the MCell data so far. It parellels the tasks. It takes the model name for example, `8` for mcell8 as an argument.
```shell
$ python avg3.py 8
```

##plotter2.py
This code produces a matplotlib plot comparing the concentration vs time graphs according the mcell model and the ode model for a particular box in the geometry. It plots the average MCell concentrations +/- standard deviations. It takes the model name and box name as arguments.
```shell
$ python plotter2.py 8 0-0-0
```
