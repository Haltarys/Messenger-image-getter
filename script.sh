#!/bin/sh

# ./script.sh to execute
# this script renames all images with a number

if [ $(basename `pwd`) != "images" ]; then
  cd images
fi

a=1
for i in *; do
  new=$(printf "%03d.png" "$a") #04 pad to length of 4
  mv -- "$i" "$new"
  a=a+1
done
