#!/usr/bin/env python
import os
import yaml
import numpy as np 
import h5py

ms = range(71, 96+1)

os.chdir(os.path.expandvars('$WELTER/sf/'))

os.getcwd()

for m in ms:

    dat_name = '../data/reduced/LkCa4_IGRINS_m{:03d}.hdf5'.format(m)
    path_out = 'm{:03d}/'.format(m)
    sf_out = 'm{:03d}/config.yaml'.format(m)
    
    f = open("m086/config.yaml")
    config = yaml.load(f)
    f.close()
    
    f=h5py.File(dat_name, "r")
    wls = f['wls'][:]
    f.close()
    
    config['data']['files'] = ['$WELTER/data/reduced/LkCa4_IGRINS_m{:03d}.hdf5'.format(m)]
    config['grid']['hdf5_path'] = '$WELTER/sf/m{:03d}/libraries/PHX_IGR_2700-4500_m{:03d}.hdf5'.format(m,m)
    lb, ub = int(np.floor(wls[0])), int(np.ceil(wls[-1]))

    config['grid']['wl_range'] = [lb, ub]
    config['PCA']['path'] = '$WELTER/sf/m{:03d}/PHX_IGR_2700-4500_K_PCA.hdf5'.format(m)
    config['data']['instruments'] =['IGRINS_K']
    
    os.makedirs(path_out, exist_ok=True)
    with open(sf_out, mode='w') as outfile:
        outfile.write(yaml.dump(config))
        print('wrote to {}'.format(path_out))

#for m in ms:
#    os.chdir("m{:03d}".format(m))
#    os.system('mkdir libraries &')
#    os.system('grid.py --create > grid.out &')
#    os.chdir("..")