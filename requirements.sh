#!/bin/bash

sudo apt-get install python3 -y && sudo apt-get install python3-pip -y
sudo pip3 install ftplib
sudo pip3 install socket
sudo pip3 install argparse

sudo chmod +x ftp_brute_forcerv2.py

echo "done"