# プロジェクト名: flag_analysis

## 概要
"全力回避フラグちゃん!" チャンネルの公開情報を取得し，グラフの可視化やデータ分析を行い，推測の実施やbot 開発などを実施していく

## やりたいこと
- 動画のタイトル，公開日，再生回数，Dead End や各フラグの登場回数をまとめたデータセットを作成し，グラフ化すること (実施済み)
  　- 他にも分析に使用できそうな項目があれば順次追加する
- 上記統計情報から，再生回数と各キャラクターや内容との相関を分析する
- サムネイル画像を識別し，クラスタリングによる教師無し機械学習を用いることで，サムネイルのイラストレーターの分類及びサムネイルと再生回数の相関を分析する
- 動画のタイトルから上記のデータセットによるラベル付けを用いた教師あり機械学習によって各フラグの登場を予測する
- 動画のタイトル情報を利用し，入力された文字列からフラグが立つかどうかを判定するbot を開発する
- YouTube Data API もしくは，Web スクレイピングを用いた上記課題の自動化
- 画像識別による各フラグ登場回の自動判定化

## 全力回避フラグちゃん! 動画情報の可視化の完全自動化タスク

### できたこと
- YouTube Data API v3 を用いて，日時の各動画の再生回数，Like，Dislike，コメント数を取得すること
- 再生回数を自動でグラフ化すること (各フラグの登場回数及びDead End 回数は目視で確認して追記している)
- 

### ファイル一覧
プログラムやプログラム内で参照及び生成されるファイルの一覧です．
※生成されたファイルを削除しない限り，1日1回の実行を前提として作成しています．

- flag_videos_info.sh
    - youtube_apikey.txt
    - $(date "+%Y-%m-%d")_flag_videos_info.json
    - videoIds.txt
    - 役割
指定したチャンネルid にアップロードされている動画のid 情報等をすべて取得し，$(date "+%Y-%m-%d")_flag_videos_info.json に出力する
また，動画id は別途videoIds.txt に出力している．
情報へのアクセスには，YouTube Data API v3 のsearch メソッドを使用している．
    
- flag_get_channel_info.sh
    - $(date "+%Y-%m-%d")_flag_channels_info.json
    - 役割
指定したチャンネルid に関する情報をすべて取得し，$(date "+%Y-%m-%d")_flag_channels_info.json に出力する
情報へのアクセスには，YouTube Data API v3 のchannels メソッドを使用しており，チャンネル登録者数や再生回数の合計といった情報が取得できる．
    
- flag_videos_stats.sh
    - $(date "+%Y-%m-%d")_flag_videos_stats.json
    - 役割
videoIds.txt に記載された動画id の動画に関する情報をすべて取得し，$(date "+%Y-%m-%d")_flag_videos_stats.json に出力する．
情報へのアクセスには，YouTube Data API v3 のvideos メソッドを使用しており，動画タイトル，公開日や再生回数，Like，DisLikeやコメント数といった情報が取得できる．
    
- flag_gen_datasets.sh
    - $(date "+%Y-%m-%d")_flag_videos_stats.csv
    - $(date "+%Y-%m-%d")_flag_videos_datasets.csv
    - flag_merge_csv.py
        - flag_encount.csv
    - 役割
$(date "+%Y-%m-%d")_flag_videos_stats.json の情報をもとに，グラフ化用のデータセット $(date "+%Y-%m-%d")_flag_videos_stats.csvを作成する．
そして，$(date "+%Y-%m-%d")_flag_videos_stats_graph.png とflag_encount.csv (Dead End，死亡フラグ，生存フラグ，恋愛フラグのカウント数を記録したファイル)を連結して，
グラフ作成用のもととなるデータセット $(date "+%Y-%m-%d")_flag_videos_datasets.csv を出力する．
    
- flag_plot_graph.sh
    - $(date "+%Y-%m-%d")_flag_videos_stats_graph.png
    - flag_videos_stats_plot.py
    - 役割
$(date "+%Y-%m-%d")_flag_videos_datasets.csv の情報をもとに，動画情報の可視化として$(date "+%Y-%m-%d")_flag_videos_stats_graph.png を出力する．

- flag_get_thumbnail.sh
    - 役割
$(date "+%Y-%m-%d")_flag_videos_stats.json の情報をもとに，各動画に存在するサムネイル画像をすべて取得する
サムネイル画像は以下のように4種類サイズが存在する．動画によっては一部ないものが存在する．
    - default (120 x 90)
    - medium (320 x 180)
    - high (480 x 360)
    - standard (640 x 480)
    - maxres (1280 x 720)
    
- flag_channel_statistics.sh
    - channel_statistics.csv
    - 役割
$(date "+%Y-%m-%d")_flag_channels_info.json から再生回数の合計とチャンネル登録者数の情報を抽出し，
日付ごとに channel_statistics.csv に日付とともに追記する．

- file_move.sh
昨日の日付のデータおよびグラフを所定のディレクトリに移動する．
    

## 関連リンク
- 全力回避フラグちゃん! https://www.youtube.com/channel/UCo_nZN5yB0rmfoPBVjYRMmw/videos
- フラグちゃんのTwitter https://twitter.com/flag__chan
- 株式会社Plott / Plott Inc. https://plott.tokyo/#top

============================================================================
# Project name: flag_analysis

## Overview.
"Avoid flag-chan at all costs!" We will get public information of the channel, visualize graphs, analyze data, make guesses, develop bots, etc.

## What we want to do
- Create a dataset of video title, release date, number of views, Dead End and number of times each flag appears, and make a graph of it (already done).
  　- If there are other items that could be used for analysis, add them sequentially.
- Analyze the correlation between the number of plays and each character or content from the above statistics.
- Identify thumbnail images and use unsupervised machine learning with clustering to classify the illustrators of thumbnails and analyze the correlation between thumbnails and the number of views.
- Predict the appearance of each flag from the title of the video using supervised machine learning with labeling by the dataset described above.
- Develop a bot that judges whether a flag appears or not from the input string using the title information of the video.
- Automate the above tasks using YouTube Data API or web scraping.
- Automatic judgment of when each flag appears by image identification.

## Avoid flags at all costs! Fully automated task for visualization of video information.

## What we did
- Using YouTube Data API v3 to get the number of views, likes, dislikes, and comments for each video on the date and time.
- (The number of times each flag appeared and the number of Dead Ends were visually checked and added.)

### File List
This is a list of files that are referenced or generated in the program or programs.
It is assumed that the program is executed once a day unless the generated files are deleted.

- flag_videos_info.sh
    - youtube_apikey.txt
    - $(date "+%Y-%m-%d")_flag_videos_info.json
    - videoIds.txt
    - Role
Obtain all the id information, etc. of the videos uploaded to the specified channel id, and output it to $(date "+%Y-%m-%d")_flag_videos_info.json
The video ids are also output separately in videoIds.txt.
To access the information, the search method of YouTube Data API v3 is used.
    
- flag_get_channel_info.sh
    - $(date "+%Y-%m-%d")_flag_channels_info.json
    - Role
Get all information about the specified channel id and output it to $(date "+%Y-%m-%d")_flag_channels_info.json
The information is accessed using the channels method of the YouTube Data API v3, which provides information such as the number of channel subscribers and the total number of views.
    
- flag_videos_stats.sh
    - $(date "+%Y-%m-%d")_flag_videos_stats.json
    - Role
Retrieves all information about the video with the video id listed in videoIds.txt, and outputs it to $(date "+%Y-%m-%d")_flag_videos_stats.json.
The videos method of the YouTube Data API v3 is used to access the information, which includes the video title, date of publication, number of views, likes, dislikes, and comments.
    
- flag_gen_datasets.sh
    - $(date "+%Y-%m-%d")_flag_videos_stats.csv
    - $(date "+%Y-%m-%d")_flag_videos_datasets.csv
    - flag_merge_csv.py
        - flag_encount.csv
    - Role
Create a dataset $(date "+%Y-%m-%d")_flag_videos_stats.csv for graphing based on the information in $(date "+%Y-%m-%d")_flag_videos_stats.json.
Then, concatenate $(date "+%Y-%m-%d")_flag_videos_stats_graph.png and flag_encount.csv (a file containing the counts of Dead End, Death Flag, Survival Flag, and Love Flag) to create a graph.
Output the dataset $(date "+%Y-%m-%d")_flag_videos_datasets.csv as the basis for creating the graph.
    
- flag_plot_graph.sh
    - $(date "+%Y-%m-%d")_flag_videos_stats_graph.png
    - flag_videos_stats_plot.py
    - Role
Output $(date "+%Y-%m-%d")_flag_videos_stats_graph.png as a visualization of video information based on the information in $(date "+%Y-%m-%d")_flag_videos_datasets.csv.

- flag_get_thumbnail.sh
    - Role
Retrieves all thumbnail images for each video based on the information in $(date "+%Y-%m-%d")_flag_videos_stats.json
Thumbnail images come in four sizes, as shown below. Some videos may not have any of these.
    - default (120 x 90)
    - medium (320 x 180)
    - high (480 x 360)
    - standard (640 x 480)
    - maxres (1280 x 720)
    
- flag_channel_statistics.sh
    - channel_statistics.csv
    - Role
Extracts the total number of views and the number of subscribers from $(date "+%Y-%m-%d")_flag_channels_info.json, and appends them to channel_statistics.csv with the date.
Add the information to channel_statistics.csv with the date.

- file_move.sh
Moves the data and graphs of yesterday's date to the specified directory.

## Related links
- Avoid flags at all costs! https://www.youtube.com/channel/UCo_nZN5yB0rmfoPBVjYRMmw/videos
- Flag-chan's Twitter: https://twitter.com/flag__chan
- Plott Inc. https://plott.tokyo/#top
