#!/bin/bash

# Run fake X server
Xvfb :99 -ac &
PID=$!
export DISPLAY=:99

# execute script
/usr/bin/python3 inverter_read.py $1

echo $?

# kill xvfb
kill -9 $PID