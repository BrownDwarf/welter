#!/usr/bin/env python
import os
import yaml

os.chdir('/home/gully/GitHub/welter/sf/')

for i in range(0,25):
    output_dir = 'eo{:03d}/output/LkCa4_so{:03d}/run03'.format(i,i)
    os.chdir(output_dir)
    
    #os.system('star.py --generate')
    #os.system('splot.py s0_o0spec.json --matplotlib')
    os.system('last_mc.py --last20k yes')
    #os.system('chain.py --files mc.hdf5 --chain')
    #os.system('mv walkers.png /home/gully/GitHub/welter/sf/plts/walkers_{}.png'.format(mdir))
    #os.system('mv plots/s0_o0spec.json.png /home/gully/GitHub/welter/sf/plts/spec_{}.png'.format(mdir))
    os.chdir('/home/gully/GitHub/welter/sf/')
