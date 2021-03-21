#!/bin/bash

path=$(pwd)
bkup="/mnt/hgfs/flag"

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


# bkup to OneDrive
for target in $(ls $(date +%Y-%m-%d)_*.png)
do
    echo "$target copies $bkup/graph"
    cp $target $bkup/graph/.
done

echo "$(date +%Y-%m-%d)_flag_videos_datasets_score.csv copies $bkup/datasets"
cp $(date +%Y-%m-%d)_flag_videos_datasets_score.csv $bkup/datasets/.

echo "flag_channel_statistics.png copies $bkup/datasets"
cp flag_channel_statistics_graph.png $bkup/graph/.

echo "flag_channel_statistics.csv copies $bkup/datasets"
cp flag_channel_statistics.csv $bkup/datasets/.

echo "all thumbnail copy $bkup/thumbnail"
cp -r --no-clobber thumbnail/* $bkup/thumbnail/

cp flag.log $bkup/datasets/.