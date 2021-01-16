#!/bin/bash

path=$(pwd)

sudo apt update -y
sudo apt install vim emacs nmap curl jq python3 python3-pip -y
sudo apt install fonts-takao -y
pip3 install update
pip3 install numpy pandas matplotlib
pip3 install config requests_oauthlib twitter

mkdir $path/data
mkdir $path/graph
mkdir $path/datasets
mkdir -p $path/thumbnail/default
mkdir -p $path/thumbnail/medium
mkdir -p $path/thumbnail/high
mkdir -p $path/thumbnail/standard
mkdir -p $path/thumbnail/maxres
