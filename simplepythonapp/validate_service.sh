#!/bin/bash

# Check if the app is running by looking for the Python process
ps aux | grep 'python3 app.py' || exit 1
