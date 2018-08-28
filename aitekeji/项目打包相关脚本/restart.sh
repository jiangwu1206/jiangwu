# 1 项目jar名称 2 分支  3 环境
if test -z $2
then
  branch='dev'
else
  branch=$2
fi

if test -z $3
then
  jvmargs='-Xms256m -Xmx512m'
else
  jvmargs=$3
fi
echo ’当前执行分支为：$branch，jvm参数为 $jvmargs ‘
cd /usr/local/dev/atms-src/$1
git pull
git checkout $branch
mvn clean install -U  -Psimulate -DskipTests=true
echo "延时1秒"
sleep 1
echo "停止$1服务"
supervisorctl stop $1
rm -rf /usr/local/deploy/webapps/
mkdir -p /usr/local/atms/$1/
cp -R /usr/local/dev/atms-src/$1/target/$1.jar /usr/local/atms/$1/
echo "延时1秒"
sleep 1
echo "启动$1服务"
supervisorctl start $1