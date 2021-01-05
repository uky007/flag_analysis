#!/bin/bash

path=$(pwd)
${path}/flag_videos_info.sh
${path}/flag_get_channel_info.sh
${path}/flag_videos_stats.sh
${path}/flag_gen_datasets.sh
${path}/flag_plot_graph.sh
${path}/flag_get_thumbnail.sh
${path}/flag_channel_statistics.sh
${path}/file_move.sh