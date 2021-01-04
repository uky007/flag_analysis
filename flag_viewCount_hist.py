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

bins = 40
maxy = 30

#データセット対象のCSV ファイル
file = sys.argv[1]
output_file = sys.argv[2]
#Date, 再生回数
num_play = pd.read_csv(file, header=0, encoding='UTF8', usecols=[3, 5], parse_dates=[0])
num_play = num_play.dropna(how='all')


# debug
#print(num_play)
#num_play.to_csv('exam_num_play.csv')

#Plot するグラフ
#Date
x = num_play[num_play.columns[0]]
#print(type(x[0]))

#再生回数
y1 = num_play[num_play.columns[1]]

#グラフの大きさ
plt.figure(figsize=(20.0, 10.0), dpi=300)
#フォント設定
#plt.rcParams['font.family'] = 'Times New Roman'
#フォント設定
#plt.rcParams['font.family'] = 'Times New Roman'
font_path = '/usr/share/fonts/truetype/takao-gothic/TakaoPGothic.ttf'
font_prop = FontProperties(fname=font_path)
matplotlib.rcParams['font.family'] = font_prop.get_name()

# グラフプロット
## 再生回数を棒グラフでプロット
play_hist = plt.hist(y1, bins=bins, color="lightblue")

        
# 軸の範囲
#plt.xlim('2019-11-01', x[len(x) - 1])
#plt.ylim([0, 3500000])
plt.ylim([0, maxy])

# グラフタイトル
plt.title("全力回避フラグちゃん! 再生回数ヒストグラム", fontname="TakaoPGothic", fontsize=20)

# 軸メモリ
plt.tick_params(axis='x', labelsize=20, labelrotation=45)
plt.tick_params(axis='y', labelsize=20)

# ラベル名
plt.xlabel("再生回数", fontsize=20, fontname="TakaoPGothic")
plt.ylabel("動画数", fontname="TakaoPGothic", fontsize=20)

## 平均値と中央値を横線でプロット
avg = plt.vlines(num_play.mean(axis=0), 0, maxy, 'b', linestyles='dashed')

# 凡例
#play_title = "再生回数"
#dead_title = "Dead End"
#shibou_title = "死亡フラグ"
#seizon_title = "生存フラグ"
#renai_title = "恋愛フラグ"
avg_title = "平均値"
#med_title = "中央値"

plt.legend([avg], [avg_title], bbox_to_anchor=(1.0, 1.0), prop={"family":"TakaoPGothic", 'size':20}, markerscale=3)

#画像保存
plt.savefig(output_file, bbox_inches="tight", pad_inches=0.0)