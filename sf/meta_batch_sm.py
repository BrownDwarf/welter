#!/usr/bin/env python

import os
import yaml

os.chdir('/home/gully/GitHub/welter/sf/')

for i in range(76, 91):
    os.chdir("m{:03d}".format(i))
    
    print('----------------------------')
    print("Starting the MCMC run.")
    print("Spawning a screen")
    screen_command = 'screen -d -m bash -c ' + '"cd /home/gully/GitHub/welter/sf/m{:03d}/output/LkCa4_sm{:03d}/run03/'.format(i, i)+'; run.sh"' 
    print(screen_command)
    os.system(screen_command)
    print(' ')

    print('Back to the start')
    os.chdir('/home/gully/GitHub/welter/sf/')
    print('----------------------------')
