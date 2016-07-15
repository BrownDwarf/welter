#!/usr/bin/env python
import os
import yaml
import numpy as np 
import h5py

#ms = range(71, 96+1)
ms = range(98, 126)

os.chdir(os.path.expandvars('$WELTER/sf/'))

for m in ms:

    path_out = 'm{:03d}/'.format(m)
    os.chdir(path_out)
    
    # Also initialize the nuissance parameter json file.
    os.system('star.py -r 2')
    os.chdir('output/mix_emcee/run02')
    os.system('star.py --initPhi')
    os.chdir(os.path.expandvars('$WELTER/sf/'))
