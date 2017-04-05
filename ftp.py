#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import socket
import time
import os
from datetime import *
from ftplib import FTP

ftp_server='IP'
ftp_user='username'
ftp_password='passowrd'
ftp_backup_dir='/dir'
 
newday = date.today()    
oldday = date.today()-timedelta(5)    
newfile = 'bakmysql-' + str(newday) + '.sql'    
oldfile = 'bakmysql-' + str(oldday) + '.sql'    
 
def upload():
    socket.setdefaulttimeout(60)    
    ftp = FTP(ftp_server)
    print("login ftp...")
    try:
        ftp.login(ftp_user, ftp_password)
        print(ftp.getwelcome())   
    except:
        print("ftp login failed.exit.")
        sys.exit()
    ftp.cwd(ftp_backup_dir)    
 
    print("upload data...")
    try:
        ftp.storbinary('STOR' + os.path.basename(newfile), open(newfile,'rb'), 1024)    
    except:
        print("upload failed. check your permission.")
    
    print("delete old file...")
    try:
        ftp.delete(os.path.basename(oldfile))    
    except:
        print("the old file in ftp doesn't exists, jumped.")
 
    print("ftp upload successful.exit...")
    ftp.quit()
 
if __name__== '__main__':
    upload()