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
git checkout $branch
git pull
mvn clean install -U  -Ptest -DskipTests=true
rm -rf /usr/local/deploy/webapps/
mkdir -p /usr/local/atms/$1/
cp -R /usr/local/dev/atms-src/$1/target/$1.jar /usr/local/atms/$1/
ps -efww|grep -w $1 |grep -v grep|cut -c 9-15|xargs kill -9
nohup java -jar $jvmargs /usr/local/atms/$1/$1.jar --spa=test --spring.profiles.active=test &
