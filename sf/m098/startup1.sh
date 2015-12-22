#!/bin/bash

mkdir libraries
mkdir plots
mkdir output

grid.py --create

pca.py --create

time pca.py --optimize=emcee --samples=30

pca.py --store --params=emcee

star.py --initPhi

star.py --generate

grep -A 4 model s0_o0spec.json

grep -A 4 data s0_o0spec.json

echo "-------------------------------------"
echo "Check the model for order-of-magnitude match to data."
echo "-------------------------------------"
read  -p "Waiting while you check.  Type any key to continue."


splot.py s0_o0spec.json --matplotlib

open plots/s0_o0spec.json.png

echo "-------------------------------------"
echo "Iteratively adjust the logOmega and plot until the continuum levels match."
echo "Copy and paste this line once you edit the config.yaml:"
echo "star.py --generate; splot.py s0_o0spec.json --matplotlib; open plots/s0_o0spec.json.png"
echo "-------------------------------------"
read  -p "Waiting while you check.  Type any key to continue."

star.py --optimize=Theta
echo "-------------------------------------"
echo "You need to manually input Theta.json into config.yaml."
echo "-------------------------------------"
read  -p "Waiting while you check.  Type any key to continue."
star.py --optimize=Cheb

star.py --run_index 1
echo "-------------------------------------"
echo "The end."
echo "-------------------------------------"