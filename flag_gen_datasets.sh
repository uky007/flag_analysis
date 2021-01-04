#!/bin/bash

target_file=$(date "+%Y-%m-%d")_flag_videos_stats.json
output_file=$(date "+%Y-%m-%d")_flag_videos_stats.csv
datasets_file=$(date "+%Y-%m-%d")_flag_videos_datasets.csv

cat ${target_file} | jq -r '.items[] | [.id, .snippet.title, .snippet.publishedAt, .snippet.description, .statistics.viewCount, .statistics.likeCount, .statistics.dislikeCount, .statistics.commentCount] | @csv' > ${output_file}
python3 flag_merge_csv.py ${output_file} ${datasets_file}