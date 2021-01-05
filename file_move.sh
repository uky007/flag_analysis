#!/bin/bash

path=$(pwd)

for target in $(ls $(date --date "1 days ago" +%Y-%m-%d)_*.png)
do
    echo "$target moves $path/graph"
    mv $target $path/graph/.
done

for target in $(ls $(date --date "1 days ago" +%Y-%m-%d)_*)
do
    echo "$target moves $path/data"
    mv $target $path/data/.
done