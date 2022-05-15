#!/bin/bash


#This is a simple automation to concatenate two files line by line.
host_file=$1
keyfile=$2
for key in  `cat $keyfile`;
do
        for line in `cat $host_file`;do echo "$line/?$key=XSS";done

done
