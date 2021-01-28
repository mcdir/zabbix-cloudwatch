#!/bin/bash

# Date:   08/08/2015
# Author: Long Chen
# Description: A script to bulk send ELB cloudwatch data to zabbix server

LIB_PATH=$(cd ../ && pwd)
PATH=$PATH:/opt/zabbix-extention/cloudwatch:${LIB_PATH}
export PATH

# Load Balancer Name
LOAD_BALANCER=$1
# AWS Account
ACCOUNT=$2
# AWS Region
REGION=$3
# Collecting 5-minute data from cloudwatch
PERIOD="300"
# Set start time and end time for collecting cloudwatch data
# Adding lag, as CloudWatch doesn't send all data if requested too early.
ENDTIME=$(date -u "+%F %H:%M:00" -d "5 minutes ago")
STARTTIME=$(date -u "+%F %H:%M:00" -d "10 minutes ago")

# Send cloudwatch data of a table to Zabbix Server
echo "zabbixCloudWatch.py --test True -a \"$ACCOUNT\" -r \"$REGION\" -s ELB -d LoadBalancerName=\"$LOAD_BALANCER\" -p \"$PERIOD\" -f \"$STARTTIME\" -t \"$ENDTIME\""
${LIB_PATH}/zabbixCloudWatch.py --test True -a "$ACCOUNT" -r "$REGION" -s "ELB" -d "LoadBalancerName=$LOAD_BALANCER" -p "$PERIOD" -f "$STARTTIME" -t "$ENDTIME"
