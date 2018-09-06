#!/bin/bash
#
#因部分UPS设备对Linux系统支持不良好而编写
#判断非UPS供电设备是否在线，不在线判断为停电状态
#

check(){
    ping -c 3 $1
    return $?
}

check $1

up=$?

for((i=0;i<5;i++))do
    if [[ 0 -ne $up ]];then
        check $1
        up=$?
        echo "$up"
    fi
done

if [[ 0 -ne $up ]];then
    echo "shutdown"
fi
