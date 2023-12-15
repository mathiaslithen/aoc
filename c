#!/bin/bash

# get day from user or default to today
if [ -z "$1" ]
then
  d=$(date '+%-d')
else
  d=$1
fi

# reset example file
rm -f ex
touch ex

# make copy for day
cp ./base.py d$d.py

# fix input str
sed -i "s/n.in/${d}.in/g" d$d.py

# fetch input for day
./get_input.py $d $2
