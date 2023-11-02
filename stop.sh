#!/bin/bash

kill -9 `ps aux | grep wxrobot | grep -v grep | awk '{print $2}'`