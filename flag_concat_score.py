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

flag_header = ["vid", "title", "date", "description", "viewCount", "likeCount", "dislikeCount", "commentCount", "DeadEndCount", "shibouflagCount", "seizonflagCount", "renaiflagCount", "score"]

output_file = sys.argv[2]

#read csv
datasets = pd.read_csv(datasets_file, header=0, index_col=0, encoding='UTF8')
print(datasets)
score = pd.read_csv(score_file, header=None, index_col=0, encoding='UTF8')
print(score)
concat_csv = pd.concat([datasets, score], axis=1)
#concat_csv.to_csv(output_file, header=True, index=True)

#flag_header = pd.read_csv(flag_header_file, header=0, encoding='UTF8')
concat_csv.columns=flag_header
concat_csv.index = np.arange(1, len(concat_csv) + 1)
concat_csv.index.name = "No."
concat_csv.to_csv(output_file, header=True, index=True, encoding='UTF8')