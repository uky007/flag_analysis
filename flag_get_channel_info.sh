#!/bin/bash

base_url="https://www.googleapis.com/youtube/v3/channels"
channel_id="UCo_nZN5yB0rmfoPBVjYRMmw"
key=$(cat youtube_apikey.txt)
part="snippet,contentDetails,status,statistics,brandingSettings"

output_file=$(date "+%Y-%m-%d")_flag_channels_info.json

api_url="${base_url}?id=${channel_id}&key=${key}&part=${part}"
echo "API Access for ${channel_id}"
curl -s ${api_url} > ${output_file}
if [ $? != 0 ]; then
        echo "An Error occurred."
        exit
fi