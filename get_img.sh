#!/bin/bash

path="/home/uky/ai/flag"
file="flag_thumbnail.csv"
base_url="https://i.ytimg.com/vi/"
img_path1="/home/uky/ai/flag/thumbnail/max"
img_path2="/home/uky/ai/flag/thumbnail/hqd"
video_path1="/maxresdefault.jpg"
video_path2="/hqdefault.jpg"

cat $path/$file | awk 'NR > 1 {print}' | while read line
do
    id=$(echo $line | cut -d ',' -f 1)
    echo $id
    title=$(echo $line | cut -d ',' -f 2)
    echo $title
    video_id=$(echo $line | cut -d ',' -f 3)
    echo ${video_id}
    echo ${base_url}
    echo ${video_path}
    #echo ${base_url}${video_id}${video_path}
    echo "${base_url}${video_id}${video_path}"
    curl "${base_url}${video_id}${video_path1}" --output ${img_path1}/${id}_${video_id}.jpg
    curl "${base_url}${video_id}${video_path2}" --output ${img_path2}/${id}_${video_id}.jpg

    if [ $? != 0 ]; then
        echo "An error occurred."
        exit
    fi
done
