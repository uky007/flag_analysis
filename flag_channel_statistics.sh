#!/bin/bash

plot_date=$(date "+%Y-%m-%d")
allviewCount=$(cat $(date "+%Y-%m-%d")_flag_channels_info.json | jq -r '.items[].statistics.viewCount')
subscriberCount=$(cat $(date "+%Y-%m-%d")_flag_channels_info.json | jq -r '.items[].statistics.subscriberCount')

target_file="channel_statistics.csv"

echo "${plot_date},${allviewCount},${subscriberCount}" >> ${target_file}