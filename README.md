# プロジェクト名: flag_analysis

## 概要
"全力回避フラグちゃん!" チャンネルの公開情報を用いて，グラフの可視化やデータ分析を用いていく

## やりたいこと
- 動画のタイトル，公開日，再生回数，Dead End や各フラグの登場回数をまとめたデータセットを作成し，グラフ化すること (実施済み)
- サムネイル画像を識別し，クラスタリングによる教師無し機械学習を用いることで，サムネイルの絵師さんの分類及びサムネイルと再生回数の相関を分析する
- 動画のタイトルから上記のデータセットによるラベル付けを用いた教師あり機械学習によって各フラグの登場を予測する
- YouTube Data API を用いた上記課題の自動化
- 画像認識による登場人物のフラグ立て

=====================================================================================================================================
# Project name: flag_analysis

## Overview.
"Avoid flag-chan at all costs!" Using graph visualization and data analysis with public information from the channel.

## What we want to do
- Create a dataset of video title, release date, number of views, Dead End, and number of appearances of each flag, and create a graph (already done)
- Identify thumbnail images and use unsupervised machine learning with clustering to classify thumbnail artists and analyze the correlation between thumbnails and the number of views.
- Predict the appearance of each flag from the title of the video using supervised machine learning with labeling using the dataset above.
- Automate the above tasks using YouTube Data API.
- Flagging of characters using image recognition
