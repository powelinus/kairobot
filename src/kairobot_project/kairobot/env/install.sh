#!/usr/bin/env bash
BASE=$1
LIDAR=$2
echo "export KAIBASE=$BASE" >> ~/.bashrc
echo "export KAILIDAR=$LIDAR" >> ~/.bashrc
source ~/.bashrc
