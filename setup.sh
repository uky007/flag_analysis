#!/bin/bash

path=$(pwd)

sudo apt update -y
sudo apt install vim emacs nmap curl jq python3 python3-pip -y
sudo apt install fonts-takao -y
sudo atp install graphviz -y
pip3 install update
pip3 install numpy pandas matplotlib sklearn dtreeviz

mkdir $path/data
mkdir $path/graph
mkdir $path/datasets
mkdir -p $path/thumbnail/default
mkdir -p $path/thumbnail/medium
mkdir -p $path/thumbnail/high
mkdir -p $path/thumbnail/maxres
