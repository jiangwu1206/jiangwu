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
cd /usr/local/dev/atms-src/tx-lcn/tx-manager
git pull
git checkout $branch
mvn clean install -U  -Ptest -DskipTests=true
mkdir -p /usr/local/atms/tx-manager/
cp -R /usr/local/dev/atms-src/tx-lcn/tx-manager/target/tx-manager.jar /usr/local/atms/tx-manager/
ps -efww|grep -w tx-manager |grep -v grep|cut -c 9-15|xargs kill -9
nohup java -jar $jvmargs /usr/local/atms/tx-manager/tx-manager.jar --spa=test --spring.profiles.active=test&
