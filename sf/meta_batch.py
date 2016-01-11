#!/usr/bin/env python


import os
import yaml

ms = range(76, 91+1)

mdirs = ['m{:03d}'.format(m) for m in ms]

os.chdir('/home/gully/GitHub/welter/sf/')

os.getcwd()

for mdir in mdirs:
    os.chdir(mdir)
    
    print('----------------------------')
    print(os.getcwd())
    print(' ')

    #print("Running startup1.sh: ")    
    #print("startup1.sh")
    #os.system('startup1.sh')
    #print("Completed startup1.sh")
    #print(' ')

    print("Starting the MCMC run.")
    out_dir = "output/LkCa4_{}/run02/".format(mdir)
    print("os.chdir(out_dir)")
    print("Spawning a screen")
    screen_command = 'screen -d -m bash -c ' + '"cd /home/gully/GitHub/welter/sf/{}/output/LkCa4_{}/run02/'.format(mdir, mdir)+'; run.sh"' 
    print(screen_command)
    os.system(screen_command)
    print(' ')

    print('Back to the start')
    os.chdir('/home/gully/GitHub/welter/sf/')
    print('----------------------------')
