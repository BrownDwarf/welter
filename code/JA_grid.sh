#!/bin/bash
#SBATCH -J JA_grid-create                  # A single job name for the array
#SBATCH --ntasks=5
#SBATCH --ntasks-per-node=5
#SBATCH --cpus-per-task=1
#SBATCH --share
#SBATCH --output=arrayJob.out
#SBATCH --error=arrayJob.err

echo $SLURM_ARRAY_TASK_ID
cd $WELTER/sf/m"${SLURM_ARRAY_TASK_ID}"
pwd
mkdir libraries
sed -i 's/Users/home/' config.yaml
grid.py --create
