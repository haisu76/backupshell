#!/bin/sh
cd /bak/bakmysql
echo "You are in bakmysql directory"
mv bakmysql* /bak/bakmysqlold
echo "Old databases are moved to bakmysqlold folder"
Now=$(date +"%Y-%m-%d")
File=bakmysql-$Now.sql
mysqldump -uusername -ppassword dbname > $File
echo "Your database backup successfully completed"
SevenDays=$(date -d -15day +"%Y-%m-%d")
if [ -f /bak/bakmysqlold/bakmysql-$SevenDays.sql ]
then
rm -rf /bak/bakmysqlold/bakmysql-$SevenDays.sql
echo "You have delete 15days ago bak file"
else
echo "15days ago bak file not exist"
fi