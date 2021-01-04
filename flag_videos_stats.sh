#!/bin/bash

base_url="https://www.googleapis.com/youtube/v3/videos"
channel_id="UCo_nZN5yB0rmfoPBVjYRMmw"
key=$(cat youtube_apikey.txt)
part="snippet,contentDetails,status,statistics,player,topicDetails,player,recordingDetails"
totalResults=$(cat videoIds.txt | wc -l)

output_file=$(date "+%Y-%m-%d")_flag_videos_stats.json

for video_id in $(tac videoIds.txt)
do
    api_url="${base_url}?id=${video_id}&key=${key}&part=${part}"
    echo "API Access for ${video_id}"
    curl -s ${api_url} >> ${output_file}
    if [ $? != 0 ]; then
        echo "An Error occurred."
        exit
    fi
done