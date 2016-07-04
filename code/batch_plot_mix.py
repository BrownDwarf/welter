#!/usr/bin/env python
import os
import yaml
import numpy as np 
import h5py

#ms = range(99, 119)
#ms = range(72, 94+1)
ms = list(range(72, 94+1)) + list(range(99, 119))

os.chdir(os.path.expandvars('$WELTER/sf/'))

os.getcwd()

for m in ms:

    dat_name = '../../data/reduced/LkCa4_IGRINS_m{:03d}.hdf5'.format(m)
    path_out = 'm{:03d}/output/mix_emcee/run01'.format(m)
    os.chdir(path_out)

    print('Plotting results from m{:03d}'.format(m))
    # Do all the grid.py and pca.py setup.
    os.system('plot_many_mix_models.py --static')
    os.system('cp mix_model.png '+
    	os.path.expandvars('$WELTER/results/fig/mix_models/mix_model_m{:03d}.png'.format(m)))
    os.chdir(os.path.expandvars('$WELTER/sf/'))
