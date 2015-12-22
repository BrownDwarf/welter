#!/bin/bash

source activate starfish

time star.py --sample=ThetaPhi --samples=50000

chain.py --files mc.hdf5 --chain
chain.py --files mc.hdf5 --triangle
chain_run.py --chain


echo "-------------------------------------"
echo "The end for now."
echo "-------------------------------------"

