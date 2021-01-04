#!/bin/bash

base_url="https://www.googleapis.com/youtube/v3/search"
channel_id="UCo_nZN5yB0rmfoPBVjYRMmw"
key=$(cat youtube_apikey.txt)
part="id,snippet"
order="date"
maxResults=50
pageToken=""

api_url="${base_url}?channelId=${channel_id}&key=${key}&part=${part}&order=${order}&maxResults=${maxResults}&pageToken=${pageToken}"
#echo ${api_url}
output_file=$(date "+%Y-%m-%d")_flag_videos_info.json
echo "API Access..."
curl -s ${api_url} --output ${output_file}
if [ $? != 0 ]; then
    echo "An Error occurred."
    exit
fi
totalResults=$(cat ${output_file} | jq -r '.pageInfo.totalResults')
pageToken=$(cat ${output_file} | jq -r '.nextPageToken')

echo $totalResults
echo $maxResults
echo $((totalResults / maxResults))

for i in $(seq $((totalResults / maxResults)))
do
    if [ ${pageToken} == null ]; then
        echo "pageToken is null."
        break
    fi
    #sleep 60
    api_url="${base_url}?channelId=${channel_id}&key=${key}&part=${part}&order=${order}&maxResults=${maxResults}&pageToken=${pageToken}"
    echo "API Access..."
    curl -s ${api_url} >> ${output_file}
    if [ $? != 0 ]; then
        echo "An Error occurred."
        exit
    fi
    pageToken=$(curl -s ${api_url} | jq -r '.nextPageToken')
done

cat ${output_file} | jq -r '.items[].id.videoId' | grep -v null > videoIds.txt