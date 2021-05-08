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
file = "flag_channel_statistics.csv"

#Date, 再生回数の合計
num_viewCounts = pd.read_csv(file, header=0, encoding='UTF8', usecols=[0, 1], parse_dates=[0])
num_viewCounts = num_viewCounts.dropna(how='all')
#Date, チャンネル登録者数
num_subscribers = pd.read_csv(file, header=0, encoding='UTF8', usecols=[0, 2], parse_dates=[0])
num_subscribers = num_subscribers.dropna(how='all')

#Plot するグラフ
#Date
x = num_subscribers[num_subscribers.columns[0]]
#print(type(x[0]))
#再生回数の合計
y1 = num_viewCounts[num_viewCounts.columns[1]]
#チャンネル登録者数
y2 = num_subscribers[num_subscribers.columns[1]]

#フォント設定
#plt.rcParams['font.family'] = 'Times New Roman'
font_path = '/usr/share/fonts/truetype/takao-gothic/TakaoPGothic.ttf'
font_prop = FontProperties(fname=font_path)
matplotlib.rcParams['font.family'] = font_prop.get_name()

#グラフの大きさ
plt.figure(figsize=(20.0, 10.0), dpi=300)
#フォント設定

fig = plt.figure(figsize=(20.0, 12.0), dpi=300)
ax1 = fig.add_subplot()


# グラフプロット
## 再生回数を棒グラフでプロット
num_viewCount = ax1.bar(x, y1, width=0.1, bottom=None, color="lightblue")

ax2 = ax1.twinx()

subscribers, = ax2.plot(x, y2, color='k')

        
# 軸の範囲
ax1.set_xlim('2021-01-04', x[len(x) - 1])
ax1.set_ylim([0,  230000000])
ax2.set_ylim([400000, 500000])

# グラフタイトル
ax1.set_title("全力回避フラグちゃん! 総再生回数とチャンネル登録者数", fontname="TakaoPGothic", fontsize=20)

# 軸メモリ
ax1.tick_params(axis='x', labelsize=20, labelrotation=45)
ax1.xaxis.set_major_locator(mdates.DayLocator(bymonthday=None, interval=7, tz=None))
ax1.tick_params(axis='y', labelsize=20)
ax2.tick_params(axis='y', labelsize=20)

# ラベル名
ax1.set_xlabel("日付", fontsize=20, fontname="TakaoPGothic")
ax1.set_ylabel("再生回数", fontname="TakaoPGothic", fontsize=20)
ax2.set_ylabel("チャンネル登録者数", fontname="TakaoPGothic", fontsize=20, rotation=270, labelpad=30)

# 凡例
view_title = "再生回数の合計"
sub_title = "チャンネル登録者数"

plt.legend([num_viewCount, subscribers], [view_title, sub_title], bbox_to_anchor=(0.2, 1.0), prop={"family":"TakaoPGothic", 'size':20}, markerscale=3)

#画像保存
plt.savefig("flag_channel_statistics_graph.png", bbox_inches="tight", pad_inches=0.0)