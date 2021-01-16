#!/bin/bash

score_file=flag_videos_score.csv
output_file=$(date "+%Y-%m-%d")_flag_videos_datasets_score.csv
datasets_file=$(date "+%Y-%m-%d")_flag_videos_datasets.csv

python3 flag_concat_score.py ${datasets_file} ${output_file}