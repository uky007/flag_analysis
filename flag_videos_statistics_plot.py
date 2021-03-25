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
#correlation coefficient
res = y1.corr(y2)
print("viewCount and likeCount corr: " + str(res))
res = y1.corr(y3)
print("viewCount and dislikeCount corr: " + str(res))
res = y1.corr(y4)
print("viewCount and commnetCount corr: " + str(res))
res = y2.corr(y3)
print("likeCount and dislikeCount corr: " + str(res))
res = y2.corr(y4)
print("likeCount and commentCount corr: " + str(res))
res = y3.corr(y4)
print("dislikeCount and commentCount corr: " + str(res))
#########################################

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
df.index = np.arange(1, len(df) + 1)
df.to_csv("flag_videos_score.csv", header=False, index=True)
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

##### Story #################################################################################
s1, = ax2.plot(x[59], y2[59], marker='*', markersize=20, color='#ff7f00', linestyle='None')
s2, = ax2.plot(x[74], y2[74], marker='*', markersize=20, color='#ff7f00', linestyle='None')
s3, = ax2.plot(x[95], y2[95], marker='*', markersize=20, color='#ff7f00', linestyle='None')
s4, = ax2.plot(x[125], y2[125], marker='*', markersize=20, color='#ff7f00', linestyle='None')
s5, = ax2.plot(x[195], y2[195], marker='*', markersize=20, color='#ff7f00', linestyle='None')
s6, = ax2.plot(x[228], y2[228], marker='*', markersize=20, color='#ff7f00', linestyle='None')
ss1, = ax2.plot(x[247], y2[247], marker='*', markersize=20, color='b', linestyle='None')
ss2, = ax2.plot(x[251], y2[251], marker='*', markersize=20, color='b', linestyle='None')
##############################################################################################
        
# 軸の範囲
ax1.set_xlim('2019-11-01', x[len(x) - 1])
ax1.set_ylim([0, 4000000])
ax2.set_ylim([0, 40000])

# max(like), avg(like)
print("Sum of likeCount:" + str(sum(y2)))
print("Max likeCount:" + str(max(y2)))
print("Average likeCount:" + str(num_like.mean(axis=0)))
print("Median likeCount:" + str(num_like.median(axis=0)))
print("Max comment count:" + str(max(y4)))
print("Average comment count:" + str(num_comment.mean(axis=0)))
print("Median comment count:" + str(num_comment.median(axis=0)))

# 分散
print("Variance of viewCount: " + str(np.var(y1)))
print("Variance of likeCount: " + str(np.var(y2)))
print("Variance of dislikeCount: " + str(np.var(y3)))
print("Variance of commentCount: " + str(np.var(y4)))

# 標準偏差
print("Std. variance of viewCount: " + str(np.std(y1)))
print("Std. variance of likeCount: " + str(np.std(y2)))
print("Std. variance of dislikeCount: " + str(np.std(y3)))
print("Std. variance of commentCount: " + str(np.std(y4)))

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
s_title = "ストーリー編"
ss_title = "サブストーリー編"

plt.legend([play, like, dislike, comment, s1, ss1], [play_title, like_title, dislike_title, comment_title, s_title, ss_title], bbox_to_anchor=(0.7, 1.0), prop={"family":"TakaoPGothic", 'size':20}, markerscale=1)

#画像保存
plt.savefig(output_file, bbox_inches="tight", pad_inches=0.0)