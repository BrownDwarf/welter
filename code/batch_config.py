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

    # Stellar parameters
    config['Theta']['grid'] = [4250.0, 3.8, 0.0]
    config['Theta']['teff2'] = 2900.0
    config['Theta']['logOmega'] = -0.2
    config['Theta']['logOmega2'] = -0.6
    config['Theta']['vsini'] = 29.0
    config['Theta']['vz'] = 11.0

    config['Theta_jump']['grid'] = [3.0, 0.003, 0.001]
    config['Theta_jump']['teff2'] = 3.0
    config['Theta_jump']['logOmega'] = 0.003
    config['Theta_jump']['logOmega2'] = 0.003
    config['Theta_jump']['vsini'] = 0.05
    config['Theta_jump']['vz'] = 0.05

    config['Theta_priors'] = '$WELTER/code/priors/user_prior.py'
    config['name'] = 'mix_emcee'
    
    config['grid']['hdf5_path'] = '$WELTER/sf/m{:03d}/libraries/PHOENIX_IGRINS_m{:03d}_Teff2700-4500.hdf5'.format(m,m)
    config['grid']['parrange'] = [[2700, 4500], [3.5, 4.0], [-0.5, 0.5]]
    config['PCA']['path'] = '$WELTER/sf/m{:03d}/PHOENIX_IGRINS_H_PCA_Teff2700-4500.hdf5'.format(m)

    #os.makedirs(path_out, exist_ok=True)
    with open(sf_out, mode='w') as outfile:
        outfile.write(yaml.dump(config))
        print('wrote to {}'.format(sf_out))