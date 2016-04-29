#!/usr/bin/env python
import os
import yaml
import numpy as np 
import h5py

ms = range(98, 125)

os.chdir(os.path.expandvars('$WELTER/sf/'))

os.getcwd()

for m in ms:

    dat_name = '../../data/reduced/LkCa4_IGRINS_m{:03d}.hdf5'.format(m)
    path_out = 'm{:03d}/'.format(m)
    os.chdir(path_out)
    sf_out = 'output/mix_emcee/run01/config.yaml'.format(m)
    
    f = open("../m115/output/mix_emcee/run01/config.yaml")
    config = yaml.load(f)
    f.close()
    
    f=h5py.File(dat_name, "r")
    wls = f['wls'][:]
    f.close()
    
    config['data']['files'] = ['$WELTER/data/reduced/LkCa4_IGRINS_m{:03d}.hdf5'.format(m)]
    config['grid']['hdf5_path'] = '$WELTER/sf/m{:03d}/libraries/PHOENIX_IGRINS_m{:03d}.hdf5'.format(m,m)
    lb, ub = int(np.floor(wls[0])), int(np.ceil(wls[-1]))

    config['grid']['wl_range'] = [lb, ub]
    config['PCA']['path'] = '$WELTER/sf/m{:03d}/PHOENIX_IGRINS_H_PCA.hdf5'.format(m)
    config['name'] = 'mix_emcee'
    config['Comments'] = 'Mixture model single order designed for use with star_mix.py'
    config['data']['instruments'] =['IGRINS_H']
    
    os.makedirs('output/mix_emcee', exist_ok=True)
    os.makedirs('output/mix_emcee/run01', exist_ok=True)
    with open(sf_out, mode='w') as outfile:
        outfile.write(yaml.dump(config))
        print('wrote to {}'.format(path_out))

    # Also initialize the nuissance parameter json file.
    os.chdir('output/mix_emcee/run01/')
    #os.system('star.py --initPhi')
    #os.system('git add -f config.yaml')
    os.system('git add -f s0_o0phi.json')
    os.chdir(os.path.expandvars('$WELTER/sf/'))
