Hi! Here is a list of the codes that I have written.

##Box Description to MCell model. 
`box_maker.py` contains functions to generate a dict() of boxes which uses `'b0_0_0'` format as the key.
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

`mcell_gen.py` import `box_maker.py` and writes all the `.mdl` files for the MCell model using the given box geometry. By default it uses '`b0_0_0'` as the release site. At the top of `mcell_gen.py` you need to specify a couple of details as per your requirements of the MCell model.
The `all_boxes.pkl` is stored in the corresponding model folder.

##run.sh
This short bash script runs the mcell model for a number of diffent seeds.
It takes `100` as in mcell100 as the first argument and `128` as in 128 seeds as the second argument.
###Here's how to use run.sh
```shell
$ ./run.sh 100 128
```

