#!/bin/bash

target_file=$(date "+%Y-%m-%d")_flag_videos_stats.json
thumbnails_path="thumbnail"

default=$(cat ${target_file} | jq -r '.items[].snippet.thumbnails.default.url')
medium=$(cat ${target_file} | jq -r '.items[].snippet.thumbnails.medium.url')
high=$(cat ${target_file} | jq -r '.items[].snippet.thumbnails.high.url')
standard=$(cat ${target_file} | jq -r '.items[].snippet.thumbnails.standard.url')
maxres=$(cat ${target_file} | jq -r '.items[].snippet.thumbnails.maxres.url')


function get_thumbnails() {
case "$1" in
    "default" ) target=$default ;;
    "medium" ) target=$medium ;;
    "high" ) target=$high ;;
    "standard" ) target=$standard ;;
    "maxres" ) target=$maxres ;;
esac

i=1
for url in $target
do
    vid=$(cat ${target_file} | jq -r '.items[].id' | head -$i | tail -1)
    if [[ ! -e  "${thumbnails_path}/$1/${i}_${vid}.jpg" ]]; then
        if [ $url != "null" ]; then 
            echo "Getting thumbnails..."
            echo $url
            curl -s $url --output "${thumbnails_path}/$1/${i}_${vid}.jpg"
            if [ $? != 0 ]; then
                echo "An Error occurred."
                exit
            fi
        else
            :
        fi
    else 
        :
    fi
    #echo $i
    i=$((i+=1))
done
}

get_thumbnails "default"
get_thumbnails "medium"
get_thumbnails "high"
get_thumbnails "standard"
get_thumbnails "maxres"