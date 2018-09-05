./restart.sh  atms-eureka dev
./restart-tx.sh dev 
./restart.sh  atms-user-center dev
./restart.sh  atms-task dev
./restart.sh  atms-wallet dev
./restart.sh  atms-incentive dev
./restart.sh  atms-trade dev
./restart.sh  atms-issue dev
./restart.sh  eth-club dev
./restart.sh  eth-club-backend dev
cd club-web/
git pull origin dev > /www/logs/atms/club-web.log
cd club-admin/
git pull origin dev > /www/logs/atms/club-admin.log
