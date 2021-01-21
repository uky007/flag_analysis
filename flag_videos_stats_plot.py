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
output = sys.argv[2]
#Date, 再生回数
num_play = pd.read_csv(file, header=0, encoding='UTF8', usecols=[3, 5], parse_dates=[0])
num_play = num_play.dropna(how='all')
#Date, Dead End
num_dead = pd.read_csv(file, header=0, encoding='UTF8', usecols=[3, 10], parse_dates=[0])
num_dead = num_dead.dropna(how='all')
#Date, 死亡フラグ
num_shibou = pd.read_csv(file, header=0, encoding='UTF8', usecols=[3, 11], parse_dates=[0])
num_shibou = num_shibou.dropna(how='all')
#Date, 生存フラグ
num_seizon = pd.read_csv(file, header=0, encoding='UTF8', usecols=[3, 12], parse_dates=[0])
num_seizon = num_seizon.dropna(how='all')
#Date, 恋愛フラグ
num_renai = pd.read_csv(file, header=0, encoding='UTF8', usecols=[3, 13], parse_dates=[0])
num_renai = num_renai.dropna(how='all')

# debug
#print(num_play)
#num_play.to_csv('exam_num_play.csv')

#Plot するグラフ
#Date
x = num_play[num_play.columns[0]]
#print(type(x[0]))

#x = pd.date_range(x[0], x[218], freq='D')
#再生回数
y1 = num_play[num_play.columns[1]]
#Dead End
y2 = num_dead[num_dead.columns[1]]
#死亡フラグ
y3 = num_shibou[num_shibou.columns[1]]
#生存フラグ
y4 = num_seizon[num_seizon.columns[1]]
#恋愛フラグ
y5 = num_renai[num_renai.columns[1]]

#グラフの大きさ
plt.figure(figsize=(20.0, 10.0), dpi=300)
#フォント設定
#plt.rcParams['font.family'] = 'Times New Roman'
font_path = '/usr/share/fonts/truetype/takao-gothic/TakaoPGothic.ttf'
font_prop = FontProperties(fname=font_path)
matplotlib.rcParams['font.family'] = font_prop.get_name()
#rcParams['font.family'] = 'sans-serif'
#rcParams['font.sans-serif'] = ['Hiragino Maru Gothic Pro', 'Yu Gothic', 'Meirio', 'Takao', 'IPAexGothic', 'IPAPGothic', 'VL PGothic', 'Noto Sans CJK JP']

# グラフプロット
## 再生回数を棒グラフでプロット
play = plt.bar(x, y1, width=1.0, bottom=None, color="lightblue")

## カウントを点でプロット
for i in range(len(x)):
    if y3[i] == 1:
        shibou, = plt.plot(x[i], y1[i], marker='s', markersize=5, color='#ff7f00', linestyle='None')

    if y2[i] == 1:
        dead, = plt.plot(x[i], y1[i], marker='*', markersize=8, color='r', linestyle='None')
    
    if y4[i] == 1:
        seizon, = plt.plot(x[i], y1[i], marker='o', markersize=4, color='c', linestyle='None')

    if y5[i] == 1:
        renai, = plt.plot(x[i], y1[i], marker='$\heartsuit$', markersize=3, color='#f781bf', linestyle='None')

## 平均値と中央値を横線でプロット
avg = plt.hlines(num_play.mean(axis=0), x[0], x[len(x) - 1], 'b', linestyles='dashed')
med = plt.hlines(num_play.median(axis=0), x[0], x[len(x) - 1], 'r', linestyles='dashed')
print("Max of viewCount:" + str(max(y1)))
print("Min of viewCount:" + str(min(y1)))
print("Average of viewCount:" + str(num_play.mean(axis=0)))
print("Median of viewCount:" + str(num_play.median(axis=0)))
        
# 軸の範囲
plt.xlim('2019-11-01', x[len(x) - 1])
plt.ylim([0, 3500000])

# グラフタイトル
plt.title("全力回避フラグちゃん! 動画集計データ", fontname="TakaoPGothic", fontsize=20)

# 軸メモリ
plt.tick_params(axis='x', labelsize=20, labelrotation=45)
plt.tick_params(axis='y', labelsize=20)

# ラベル名
plt.xlabel("動画公開日", fontsize=20, fontname="TakaoPGothic")
plt.ylabel("再生回数", fontname="TakaoPGothic", fontsize=20)

# 凡例
play_title = "再生回数"
dead_title = "Dead End"
shibou_title = "死亡フラグ"
seizon_title = "生存フラグ"
renai_title = "恋愛フラグ"
avg_title = "平均値"
med_title = "中央値"

plt.legend([play, dead, shibou, seizon, renai, avg, med], [play_title, dead_title, shibou_title, seizon_title, renai_title, avg_title, med_title], bbox_to_anchor=(1.0, 1.0), prop={"family":"TakaoPGothic", 'size':20}, markerscale=3)

#画像保存
plt.savefig(output, bbox_inches="tight", pad_inches=0.0)