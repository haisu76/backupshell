
MSBackup V1.0

本文件包含两个部分，1为数据库备份导出，2为文件ftp上传至异地。

1、backshell.sh 备份mysql数据库，共保留15天，循环删除15天之前的。

2、ftp.py python脚本，用于将备份的数据库文件将上传到某个ftp服务器的指定目录。


备注：需要运行此脚本的服务器需要安装python环境。

     将backupshell文件加入crontab开机运行。

// Designed by Haisu 2017-4-5