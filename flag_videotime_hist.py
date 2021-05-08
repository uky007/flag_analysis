import os
import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime
import matplotlib.dates as mdates
import matplotlib.patches as mpatches
from matplotlib.path import Path
import matplotlib
from matplotlib.font_manager import FontProperties
from matplotlib import rcParams
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

bins = 15
maxy = 60

#データセット対象のCSV ファイル
file = sys.argv[1]
output_file = sys.argv[2]
#Date, 再生回数
num_play = pd.read_csv(file, header=0, encoding='UTF8', usecols=[3, 5], parse_dates=[0])
num_play = num_play.dropna(how='all')
#Date, 動画時間
num_time = pd.read_csv(file, header=0, encoding='UTF8', usecols=[3, 9], parse_dates=[0])
num_time = num_time.dropna(how='all')


#Plot するグラフ
#Date
x = num_play[num_play.columns[0]]

#再生回数
y1 = num_play[num_play.columns[1]]
#動画時間
#y9 = num_time[num_time.columns[1]]

seconds = []
y9 = []
y10 = []

for i in range(len(x)):
    try:
        dt = datetime.datetime.strptime(num_time[num_time.columns[1]][i], "PT%MM%SS")
    except ValueError:
        try:
            dt = datetime.datetime.strptime(num_time[num_time.columns[1]][i], "PT%MM")
        except ValueError:
            dt = datetime.datetime.strptime(num_time[num_time.columns[1]][i], "PT%SS")
    
    y9.append(dt.time())
    sec = dt.minute * 60 + dt.second
    y10.append(sec)

vt_seconds = pd.Series(y10)
#フォント設定
font_path = '/usr/share/fonts/truetype/takao-gothic/TakaoPGothic.ttf'
font_prop = FontProperties(fname=font_path)
matplotlib.rcParams['font.family'] = font_prop.get_name()

fig = plt.figure(figsize=(20.0, 12.0), dpi=300)

#グラフの大きさ
#ax1.figure(figsize=(20.0, 10.0), dpi=300)

# グラフプロット
## 再生回数を棒グラフでプロット
time_hist = plt.hist(y9, bins=bins, color="lightblue")

plt.tick_params(axis='x', labelsize=20, labelrotation=45)
plt.tick_params(axis='y', labelsize=20)

# グラフタイトル
plt.title("全力回避フラグちゃん! 動画時間のヒストグラム", fontname="TakaoPGothic", fontsize=20)

# 軸メモリ

## 平均値と中央値を線でプロット
avg = plt.vlines(vt_seconds.mean(axis=0), 0, maxy, 'b', linestyles='dashed')
med = plt.vlines(vt_seconds.median(axis=0), 0, maxy, 'r', linestyles='dashed')


binnedvideotime = pd.cut(y10, bins)
print(binnedvideotime.value_counts())

# ラベル名
plt.xlabel("動画時間", fontsize=20, fontname="TakaoPGothic")
plt.ylabel("動画数", fontname="TakaoPGothic", fontsize=20, labelpad=30)

# 凡例
avg_title = "平均値"
med_title = "中央値"

plt.legend([avg, med], [avg_title, med_title], bbox_to_anchor=(1.0, 1.0), prop={"family":"TakaoPGothic", 'size':20}, markerscale=1)

#画像保存
plt.savefig(output_file, bbox_inches="tight", pad_inches=0.0)