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
import numpy.polynomial.polynomial as P


#データセット対象のCSV ファイル
file = sys.argv[1]
#output_file = sys.argv[2]
#Date, 再生回数
num_play = pd.read_csv(file, header=0, encoding='UTF8', usecols=[3, 5], parse_dates=[0])
num_play = num_play.dropna(how='all')
#Date, 動画時間
num_time = pd.read_csv(file, header=0, encoding='UTF8', usecols=[3, 9], parse_dates=[0])
num_time = num_time.dropna(how='all')
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
#print(x)
#print(type(x[0]))

#x = pd.date_range(x[0], x[218], freq='D')
#再生回数
y1 = num_play[num_play.columns[1]]
#動画時間
#y9 = num_time[num_time.columns[1]]
#Like
y2 = num_like[num_like.columns[1]]
#DisLike
y3 = num_dislike[num_dislike.columns[1]]
#コメント
y4 = num_comment[num_comment.columns[1]]


seconds = []
y9 = []
y10 = []

for i in range(len(x)):
    try:
        dt = datetime.datetime.strptime(num_time[num_time.columns[1]][i], "PT%MM%SS")
    except ValueError:
        dt = datetime.datetime.strptime(num_time[num_time.columns[1]][i], "PT%MM")
    
    y9.append(dt.time())
    sec = dt.minute * 60 + dt.second
    y10.append(sec)

vt_seconds = pd.Series(y10)

#print(vt_seconds)

#res = y1.corr(vt_seconds)
#print("viewCount and videoTime corr:" + str(res))

#フォント設定
font_path = '/usr/share/fonts/truetype/takao-gothic/TakaoPGothic.ttf'
font_prop = FontProperties(fname=font_path)
matplotlib.rcParams['font.family'] = font_prop.get_name()

fig = plt.figure(figsize=(10.0, 10.0), dpi=300)
ax1 = fig.add_subplot()

#グラフの大きさ
#ax1.figure(figsize=(20.0, 10.0), dpi=300)

# グラフプロット
## 再生回数と動画時間の散布図をプロット
sc = plt.scatter(y3, y1, s=50, c="b", alpha=0.5, linewidths=1, edgecolors="k")
#plt.colorbar()


coef = P.polyfit(y3, y1, 1)
 
# 作成した多項式近似を表示
print("viewCount & dislikeCount approximate: " + 'y = ' + str(coef[0]) + ' + ' + str(coef[1]) + ' * x')

line = P.polyval(y3,coef)

approximate, = plt.plot(y3, line, color='k')
        
# 軸の範囲
plt.xlim([0, 5000])
plt.ylim([0, 4000000])

# グラフタイトル
plt.title("全力回避フラグちゃん! 再生回数と低評価数\n 散布図", fontname="TakaoPGothic", fontsize=10)

# 軸メモリ
plt.tick_params(axis='x', labelsize=10, labelrotation=45)
plt.tick_params(axis='y', labelsize=10)


# ラベル名
plt.xlabel("低評価数", fontsize=10, fontname="TakaoPGothic")
plt.ylabel("再生回数", fontname="TakaoPGothic", fontsize=10)

# 凡例
sc_title = "動画"
approximate_title = "近似曲線"

plt.legend([sc, approximate], [sc_title, approximate_title], bbox_to_anchor=(1.0, 1.0), prop={"family":"TakaoPGothic", 'size':10}, markerscale=1)

#画像保存
plt.savefig("flag_viewCount_dislikeCount_scatter_graph.png", bbox_inches="tight", pad_inches=0.0)