#!/bin/bash

input_file=$(date "+%Y-%m-%d")_flag_videos_datasets.csv
stats_output_file=$(date "+%Y-%m-%d")_flag_videos_stats_graph.png
hist_output_file=$(date "+%Y-%m-%d")_flag_viewCount_hist_graph.png
statistics_output_file=$(date "+%Y-%m-%d")_flag_videos_statistics_graph.png
videotime_viewcount_file=$(date "+%Y-%m-%d")_flag_videotime_viewcount_graph.png
videotime_hist_file=$(date "+%Y-%m-%d")_flag_videotime_hist_graph.png

python3 flag_videos_stats_plot.py ${input_file} ${stats_output_file}
python3 flag_viewCount_hist.py ${input_file} ${hist_output_file}
python3 flag_videos_statistics_plot.py ${input_file} ${statistics_output_file}
python3 flag_videotime_viewcount.py ${input_file} ${videotime_viewcount_file}
python3 flag_videotime_hist.py ${input_file} ${videotime_hist_file}
python3 flag_viewcount_videotime_scatter.py ${input_file}
python3 flag_viewcount_likecount_scatter.py ${input_file}
python3 flag_viewcount_dislikecount_scatter.py ${input_file}
python3 flag_viewcount_commentcount_scatter.py ${input_file}
python3 flag_viewcount_likecount_dislikecount_bubble.py ${input_file}