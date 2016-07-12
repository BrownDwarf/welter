#!/usr/bin/env python
import os
import yaml
import numpy as np 
#import h5py

ms = range(98, 126)

os.chdir(os.path.expandvars('$WELTER/sf/'))

os.getcwd()

for m in ms:

    path_out = 'm{:03d}/'.format(m)
    sf_out = 'm{:03d}/config.yaml'.format(m)

    # Presuppose that the file exists...    
    f = open("m{:03d}/config.yaml".format(m))
    config = yaml.load(f)
    f.close()
    
    config['grid']['hdf5_path'] = '$WELTER/sf/m{:03d}/libraries/PHOENIX_IGRINS_m{:03d}_Teff2700-4500.hdf5'.format(m,m)

    config['grid']['parrange'] = [[2700, 4500], [3.5, 4.0], [-0.5, 0.5]]
    config['PCA']['path'] = '$WELTER/sf/m{:03d}/PHOENIX_IGRINS_H_PCA_Teff2700-4500.hdf5'.format(m)
    print("{}".format(sf_out))
    
    os.makedirs(path_out, exist_ok=True)
    with open(sf_out, mode='w') as outfile:
        outfile.write(yaml.dump(config))
        print('wrote to {}'.format(path_out))

#for m in ms:
    #os.chdir("m{:03d}".format(m))
    #os.system('mkdir libraries &')
    #os.system('grid.py --create > grid.out &')
    #os.chdir("..")

