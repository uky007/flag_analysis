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
#Date, Like
num_like = pd.read_csv(file, header=0, encoding='UTF8', usecols=[3, 6], parse_dates=[0])
num_like = num_like.dropna(how='all')
#Date, DisLike
num_dislike = pd.read_csv(file, header=0, encoding='UTF8', usecols=[3, 7], parse_dates=[0])
num_dislike = num_dislike.dropna(how='all')
#Date, コメント数
num_comment = pd.read_csv(file, header=0, encoding='UTF8', usecols=[3, 8], parse_dates=[0])
num_comment = num_comment.dropna(how='all')

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
#Like
y2 = num_like[num_like.columns[1]]
#DisLike
y3 = num_dislike[num_dislike.columns[1]]
#コメント
y4 = num_comment[num_comment.columns[1]]

#########################################
#Score
vn = []
ln = []
score = []

for i in range(len(num_play)):
    vn.append((y1[i] - min(y1)) / (max(y1) - min(y1)))
    ln.append((y2[i] - min(y2)) / (max(y2) - min(y2)))
    score.append(vn[i] * ln[i] * 100)

df = pd.DataFrame(score)
df.to_csv("flag_videos_score.csv", header=False, index=False)
##########################################


#フォント設定
#plt.rcParams['font.family'] = 'Times New Roman'
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
like, = ax2.plot(x, y2, color='r')
dislike, = ax2.plot(x, y3, color='b')
comment, = ax2.plot(x, y4, color='k')
        
# 軸の範囲
ax1.set_xlim('2019-11-01', x[len(x) - 1])
ax1.set_ylim([0, 3500000])
ax2.set_ylim([0, 30000])

# max(like), avg(like)
print("Max likeCount:" + str(max(y2)))
print("Average likeCount:" + str(num_like.mean(axis=0)))
print("Median likeCount:" + str(num_like.median(axis=0)))
print("Max comment count:" + str(max(y4)))
print("Average comment count:" + str(num_comment.mean(axis=0)))
print("Median comment count:" + str(num_comment.median(axis=0)))

# グラフタイトル
ax1.set_title("全力回避フラグちゃん! 再生回数と評価数", fontname="TakaoPGothic", fontsize=20)

# 軸メモリ
ax1.tick_params(axis='x', labelsize=20, labelrotation=45)
ax1.tick_params(axis='y', labelsize=20)
ax2.tick_params(axis='y', labelsize=20)

# ラベル名
ax1.set_xlabel("動画公開日", fontsize=20, fontname="TakaoPGothic")
ax1.set_ylabel("再生回数", fontname="TakaoPGothic", fontsize=20)
ax2.set_ylabel("評価/コメント数", fontname="TakaoPGothic", fontsize=20, rotation=270, labelpad=30)

# 凡例
play_title = "再生回数"
like_title = "高評価"
dislike_title = "低評価"
comment_title = "コメント"

plt.legend([play, like, dislike, comment], [play_title, like_title, dislike_title, comment_title], bbox_to_anchor=(1.0, 1.0), prop={"family":"TakaoPGothic", 'size':20}, markerscale=3)

#画像保存
plt.savefig(output_file, bbox_inches="tight", pad_inches=0.0)