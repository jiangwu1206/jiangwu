#!/bin/bash
#backup MongoDB

#mongodump命令路径
DUMP=/usr/local/mongodb/bin/mongodump
#临时备份目录
OUT_DIR=/mnt/lost+found/db/mongodb/mongodb_bak_now
#备份存放路径
TAR_DIR=/mnt/lost+found/db/mongodb/mongodb_bak_list
#获取当前系统时间
DATE=`date '+%y_%m_%d_%H_%M'`
#数据库
DB_NAME=whotel_db
DB_NAME2=whotel_branch
#数据库账号
DB_USER=gshis
#数据库密码
DB_PASS=jxd83664567
#DAYS=7代表删除7天前的备份，即只保留近7天的备份
DAYS=7
#最终保存的数据库备份文件
TAR_BAK="mongodb_bak_$DATE.tar.gz"

cd $OUT_DIR

rm -rf $OUT_DIR/*

mkdir -p $OUT_DIR/$DATE

#备份全部数据库

#$DUMP -h 15.62.32.112:27017 -u $DB_USER -p $DB_PASS --authenticationDatabase "admin" -o $OUT_DIR/$DATE
$DUMP -u $DB_USER -p $DB_PASS -d $DB_NAME -o $OUT_DIR/$DATE
$DUMP -u $DB_USER -p $DB_PASS -d $DB_NAME2 -o $OUT_DIR/$DATE

#压缩为.tar.gz格式
tar -zcvf $TAR_DIR/$TAR_BAK $OUT_DIR/$DATE

#删除15天前的备份文件 
find $TAR_DIR/ -mtime +$DAYS -delete

exit
