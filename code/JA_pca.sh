#!/bin/bash

echo $SLURM_ARRAY_TASK_ID
cd $WELTER/sf/m"$(printf "%03d\n" $SLURM_ARRAY_TASK_ID)"
pwd
pca.py --create
pca.py --optimize=emcee --samples=20
pca.py --store --params=emcee
