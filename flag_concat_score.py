import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime
import matplotlib.dates as mdates
import matplotlib.patches as mpatches
import os
import sys
from matplotlib.path import Path
from pandas.plotting import register_matplotlib_converters


#to merge target files
datasets_file = sys.argv[1]
score_file = "flag_videos_score.csv"
rank_file = "flag_rank.csv"
anken_file = "flag_anken.csv"
meta_file = "flag_meta_info.csv"

flag_header = ["vid", "title", "date", "description", "viewCount", "likeCount", "dislikeCount", "commentCount", "videoTime", "DeadEndCount", "shibouflagCount", "seizonflagCount", "renaiflagCount", "collabo", "story", "sub-story", "flagra", "shorts", "rank", "anken", "score"]
flag_meta_header = ["collabo", "story", "sub-story", "flagra", "shorts", "rank", "anken", "score"]

output_file = sys.argv[2]
output_meta_file = "flag_video_meta_info.csv"

#read csv
datasets = pd.read_csv(datasets_file, header=0, index_col=0, encoding='UTF8')
#print(datasets)
score = pd.read_csv(score_file, header=None, index_col=0, encoding='UTF8')
#print(score)
rank = pd.read_csv(rank_file, header=None, index_col=None, na_values=['N/A'], encoding='UTF8')
rank.index = np.arange(1, len(rank) + 1)

anken = pd.read_csv(anken_file, header=None, index_col=None, na_values=['N/A'], encoding='UTF8')
anken.index = np.arange(1, len(anken) + 1)

meta = pd.read_csv(meta_file, header=None, index_col=None, na_values=['N/A'], encoding='UTF8', skiprows=1)
meta.index = np.arange(1, len(anken) + 1)

concat_meta_info_csv = pd.concat([meta, rank, anken, score], axis=1)
concat_meta_info_csv.columns=flag_meta_header
concat_meta_info_csv.index = np.arange(1, len(concat_csv) + 1)
concat_meta_info_csv.index.name = "No."
concat_meta_info_csv.to_csv(output_meta_file, header=True, index=True)

#concat_csv = pd.concat([datasets, rank, anken, score], axis=1)
concat_csv = pd.concat([datasets, meta, rank, anken, score], axis=1)
#concat_csv.to_csv(output_file, header=True, index=True)


#flag_header = pd.read_csv(flag_header_file, header=0, encoding='UTF8')
concat_csv.columns=flag_header
concat_csv.index = np.arange(1, len(concat_csv) + 1)
concat_csv.index.name = "No."
concat_csv.to_csv(output_file, header=True, index=True, encoding='UTF8')