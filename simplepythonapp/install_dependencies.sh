#!/bin/bash

# Install Python3 and pip3 if not already installed
sudo apt-get update
sudo apt-get install -y python3 python3-pip

# Install Python dependencies from requirements.txt
cd /home/ec2-user/simplepythonapp
pip3 install -r requirements.txt
