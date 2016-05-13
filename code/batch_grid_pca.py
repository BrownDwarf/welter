#!/usr/bin/env python
import os
import yaml
import numpy as np 
import h5py

#ms = range(98, 125)
ms = range(71, 96+1)

os.chdir(os.path.expandvars('$WELTER/sf/'))

os.getcwd()

for m in ms:

    path_out = 'm{:03d}/'.format(m)
    os.chdir(path_out)

    # Do all the grid.py and pca.py setup.
    os.system('grid.py --create')
    os.system('pca.py --create')
    os.system('pca.py --optimize=emcee --samples=30')
    os.system('pca.py --store --params=emcee')
    os.chdir(os.path.expandvars('$WELTER/sf/'))
