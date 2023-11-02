#!/bin/bash

./stop.sh
sleep 0.5

nohup python3 -u wxrobot.py > server.log &