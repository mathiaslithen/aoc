#!/bin/bash

# get day
d=$(date '+%d')

# make copy for day
cp ./base.py d$d.py

# fix input str
sed -i "s/n.in/${d}.in/g" d$d.py

# fetch input for day
./get_input.py
