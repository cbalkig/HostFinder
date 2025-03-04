#!/bin/bash
# check.sh

./.venv/bin/python3 -m pip install --upgrade pip
./.venv/bin/python3 -m pip install -r requirements.txt
sudo ./.venv/bin/python3 main.py --p 192.168.0

#http://tplinkrepeater.net/