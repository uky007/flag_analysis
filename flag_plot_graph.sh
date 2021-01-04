#!/bin/bash

input_file=$(date "+%Y-%m-%d")_flag_videos_datasets.csv
output_file=$(date "+%Y-%m-%d")_flag_videos_stats_graph.png

python3 flag_videos_stats_plot.py ${input_file} ${output_file}