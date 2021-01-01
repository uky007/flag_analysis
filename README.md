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

## 関連リンク
- 全力回避フラグちゃん! https://www.youtube.com/channel/UCo_nZN5yB0rmfoPBVjYRMmw/videos
- フラグちゃんのTwitter https://twitter.com/flag__chan
- 株式会社Plott / Plott Inc. https://plott.tokyo/#top

====================================================================================
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

## Related links
- Avoid flags at all costs! https://www.youtube.com/channel/UCo_nZN5yB0rmfoPBVjYRMmw/videos
- Flag-chan's Twitter: https://twitter.com/flag__chan
- Plott Inc. https://plott.tokyo/#top
