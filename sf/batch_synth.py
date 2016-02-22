#!/usr/bin/env python

import os
import yaml


os.chdir('/home/gully/GitHub/welter/sf/')

for i in range(76, 91):
    print(i)
    os.chdir('m{:03d}/'.format(i))

    with open('config.yaml', mode='r') as f:
        config = yaml.load(f)    
    
    #These will be our initial guesses.
    config['Comments'] = "SYNTHETIC DATA simulating two-Temps: 3300 and 4100. The 4100 filling factor is 70 percent."
    config['Theta']['grid'] = [4000.0, 3.7, 0.0]
    config['Theta']['logOmega'] = -0.22
    config['Theta']['vsini'] = 30.0
    config['Theta']['vz'] = 92.0
    config['name'] = "LkCa4_sm{:03d}".format(i)
    config['data']['files'] = ["/home/gully/GitHub/welter/data/synthetic/LkCa4_Synthetic_sm{:03d}.hdf5".format(i)]
    config['grid']['hdf5_path'] = "/home/gully/GitHub/welter/sf/m{:03d}/libraries/PHOENIX_IGRINS_m{:03d}.hdf5".format(i,i)
    config['Phi'] = {"l": 25.0, "logAmp": -2.7, "sigAmp": 0.3}
    with open('config.yaml', mode='w') as f:
        f.write(yaml.dump(config))

    os.system('star.py --run_index 3')

    os.chdir('/home/gully/GitHub/welter/sf/')
