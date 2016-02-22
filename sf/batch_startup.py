#!/usr/bin/env python

import os
import yaml

ms = range(98, 125+1)

mdirs = ['m{:03d}'.format(m) for m in ms]

os.chdir('/home/gully/GitHub/welter/sf/')


for mdir in mdirs:
    os.chdir(mdir)
    print(os.getcwd())

    if os.path.isfile('eparams_emcee.npy'):
        print('Skipping mdir')
    else:
        os.system('startup1.sh')
        #os.system('echo "Dry run"')

    os.chdir('..')
