#!/bin/bash
path=$1
n_threads=$2
mkdir -p downloaded_images
for i in $(seq 1 1 $n_threads); do
    j=$((i-1))
    python download_pictures.py $path $n_threads $j &
    echo launched process $i
done
wait
echo "DONE :)"