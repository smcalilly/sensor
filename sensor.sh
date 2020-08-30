#!/bin/bash
cd "$(dirname "$0")";
CWD="$(pwd)"
echo $CWD
sudo python3 /home/sam/sensor/main.py
