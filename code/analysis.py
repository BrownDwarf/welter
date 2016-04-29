#!/usr/bin/env python


import os
import yaml

ms = list(range(76, 91+1)) + list(range(99, 111+1)) + [115, 116, 117]

mdirs = ['m{:03d}'.format(m) for m in ms]

os.chdir('/home/gully/GitHub/welter/sf/')

for mdir in mdirs:
    output_dir = '/output/LkCa4_{}/run01/'.format(mdir)
    os.chdir(mdir+output_dir)
    
    os.system('star.py --generate')
    os.system('splot.py s0_o0spec.json --matplotlib')
    #os.system('last_mc.py --last20k yes')
    #os.system('chain.py --files mc.hdf5 --chain')
    #os.system('mv walkers.png /home/gully/GitHub/welter/sf/plts/walkers_{}.png'.format(mdir))
    os.system('mv plots/s0_o0spec.json.png /home/gully/GitHub/welter/sf/plts/spec_{}.png'.format(mdir))
    os.chdir('/home/gully/GitHub/welter/sf/')
