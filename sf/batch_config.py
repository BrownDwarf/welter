#!/usr/bin/env python


import os
import yaml

ms = range(98, 125+1)

mdirs = ['m{:03d}'.format(m) for m in ms]

os.chdir('/home/gully/GitHub/welter/sf/')

os.getcwd()

for mdir in mdirs:
    os.chdir(mdir)
    print(os.getcwd())
    
    f = open("config.yaml")
    config = yaml.load(f)
    f.close()

    val = config['data']['files']
    if type(val) != list:
        config['data']['files'] = [val]

    with open("config.yaml", mode='w') as outfile:
        outfile.write(yaml.dump(config))
        print('Revised the config.yaml file: data file is 1 element list.')
    os.chdir('..')

