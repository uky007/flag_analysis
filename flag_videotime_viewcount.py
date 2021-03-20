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


#データセット対象のCSV ファイル
file = sys.argv[1]
output_file = sys.argv[2]
#Date, 再生回数
num_play = pd.read_csv(file, header=0, encoding='UTF8', usecols=[3, 5], parse_dates=[0])
num_play = num_play.dropna(how='all')
#Date, 再生時間
num_time = pd.read_csv(file, header=0, encoding='UTF8', usecols=[3, 9], parse_dates=[0])
num_time = num_time.dropna(how='all')


# debug
#print(num_play)
#num_play.to_csv('exam_num_play.csv')

#Plot するグラフ
#Date
x = num_play[num_play.columns[0]]
#print(x)
#print(type(x[0]))

#x = pd.date_range(x[0], x[218], freq='D')
#再生回数
y1 = num_play[num_play.columns[1]]
#再生時間
#y9 = num_time[num_time.columns[1]]

seconds = []
y9 = []

for i in range(len(x)):
    try:
        dt = datetime.datetime.strptime(num_time[num_time.columns[1]][i], "PT%MM%SS")
    except ValueError:
        dt = datetime.datetime.strptime(num_time[num_time.columns[1]][i], "PT%MM")
    
    y9.append(dt.time())
    #print(y9[i])
    
#print(len(y9))
#print(y9)

#res = y1.corr(y9)
#print("viewCount and videoTime corr:" + str(res))

#フォント設定
font_path = '/usr/share/fonts/truetype/takao-gothic/TakaoPGothic.ttf'
font_prop = FontProperties(fname=font_path)
matplotlib.rcParams['font.family'] = font_prop.get_name()

fig = plt.figure(figsize=(20.0, 12.0), dpi=300)
ax1 = fig.add_subplot()

#グラフの大きさ
#ax1.figure(figsize=(20.0, 10.0), dpi=300)

# グラフプロット
## 再生回数を棒グラフでプロット
play = ax1.bar(x, y1, width=1.0, bottom=None, color="lightblue")

## Like, Dislike, Commnetを折れ線でプロット
ax2 = ax1.twinx()
time, = ax2.plot(x, y9, color='r')


        
# 軸の範囲
ax1.set_xlim('2019-11-01', x[len(x)-1])
ax1.set_ylim([0, 3600000])
ax2.set_ylim([0, '00:15:00'])

# グラフタイトル
ax1.set_title("全力回避フラグちゃん! 再生回数と動画時間", fontname="TakaoPGothic", fontsize=20)

# 軸メモリ
ax1.tick_params(axis='x', labelsize=20, labelrotation=45)
ax1.tick_params(axis='y', labelsize=20)
ax2.tick_params(axis='y', labelsize=20)

## 平均値と中央値を横線でプロット
#avg = ax1.hlines(num_play[220:].mean(axis=0), x[0], '2021-01-31', 'b', linestyles='dashed')
#med = ax1.hlines(num_play[220:].median(axis=0), x[0], '2021-01-31', 'r', linestyles='dashed')
#print("Average of viewCount:" + str(num_play[220:].mean(axis=0)))
#print("Median of viewCount:" + str(num_play[220:].median(axis=0)))

# ラベル名
ax1.set_xlabel("動画公開日", fontsize=20, fontname="TakaoPGothic")
ax1.set_ylabel("再生回数", fontname="TakaoPGothic", fontsize=20)
ax2.set_ylabel("動画時間", fontname="TakaoPGothic", fontsize=20, rotation=270, labelpad=30)

# 凡例
play_title = "再生回数"
vt_title = "動画時間"

plt.legend([play, time], [play_title, vt_title], bbox_to_anchor=(1.0, 1.0), prop={"family":"TakaoPGothic", 'size':20}, markerscale=1)

#画像保存
plt.savefig(output_file, bbox_inches="tight", pad_inches=0.0)