#!/usr/bin/env python

import os
import yaml

os.chdir('/home/gully/GitHub/welter/sf/')

for i in range(0, 25):
    os.chdir("eo{:03d}".format(i))
    
    print('----------------------------')
    print("Starting the MCMC run.")
    out_dir = "output/LkCa4_so{:03d}/run03/".format(i)
    print("Spawning a screen")
    screen_command = 'screen -d -m bash -c ' + '"cd /home/gully/GitHub/welter/sf/eo{:03d}/output/LkCa4_so{:03d}/run03/'.format(i, i)+'; run.sh"' 
    print(screen_command)
    os.system(screen_command)
    print(' ')

    print('Back to the start')
    os.chdir('/home/gully/GitHub/welter/sf/')
    print('----------------------------')
