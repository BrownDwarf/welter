#!/usr/bin/env python
import os
import yaml
import numpy as np 
import h5py

ms = range(100, 117)
#ms = range(72, 94+1)
#ms = list(range(72, 94+1)) + list(range(99, 119))

os.chdir(os.path.expandvars('$WELTER/sf/'))

os.getcwd()

for m in ms:

    path_out = 'm{:03d}/output/mix_emcee/run02'.format(m)
    os.chdir(path_out)

    print('Plotting results from m{:03d}'.format(m))
    os.system('cp temp_emcee_chain.npy emcee_chain.npy')
    os.system('plot_many_mix_models.py --static')
    os.system('cp mix_model.png '+
    	os.path.expandvars('$WELTER/results/fig/mix_models_run02/mix_model_m{:03d}.png'.format(m)))
    os.chdir(os.path.expandvars('$WELTER/sf/'))
