#!/usr/bin/env python

import os
import yaml
import numpy as np 
import h5py

ms = range(71, 96+1)

os.chdir(os.path.expandvars('$WELTER/sf/'))

os.getcwd()

for m in ms:

    path_out = 'm{:03d}/output/mix_emcee/run01/'.format(m)
    os.chdir(path_out)

    # Use sbatch.
    os.system('sbatch --job-name=m{:03d} star_mix.py --samples=5000 --incremental_save=50'.format(m))
    os.chdir(os.path.expandvars('$WELTER/sf/'))
