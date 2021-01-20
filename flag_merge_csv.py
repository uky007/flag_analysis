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
videos_stats_file = sys.argv[1]
flag_encount_file = "flag_encount.csv"
flag_header_file = "flag_header.csv"

flag_header = ["vid", "title", "date", "description", "viewCount", "likeCount", "dislikeCount", "commentCount", "videoTime", "DeadEndCount", "shibouflagCount", "seizonflagCount", "renaiflagCount"]

output_file = sys.argv[2]

#read csv
videos_stats = pd.read_csv(videos_stats_file, header=None, encoding='UTF8')
flag_encount = pd.read_csv(flag_encount_file, header=None, encoding='UTF8')
concat_csv = pd.concat([videos_stats, flag_encount], axis=1)
#concat_csv.to_csv(output_file, header=True, index=True)

#flag_header = pd.read_csv(flag_header_file, header=0, encoding='UTF8')
concat_csv.columns=flag_header
concat_csv.index = np.arange(1, len(concat_csv) + 1)
concat_csv.index.name = "No."
concat_csv.to_csv(output_file, header=True, index=True, encoding='UTF8')