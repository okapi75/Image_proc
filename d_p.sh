#!/bin/bash

addr=$1
num=$2

#echo 'process time' >> runtime.txt

for i in $(seq 5 1 $num);
do
	START=$(date +%s%N)
	bash multiprocess.sh $addr $i
	END=$(date +%s%N)
	DIFF=$(($(( $END - $START ))/100000))
        
	echo -n $i ' ' >> runtime.txt
        echo $DIFF >> runtime.txt
        rm -r downloaded_images	
done

column -t -s ' ' runtime.txt >> runtime1.txt
rm runtime.txt
