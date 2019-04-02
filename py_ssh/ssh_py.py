#-*- coding: utf-8 -*-
#!/usr/bin/python
import paramiko
import datetime
import os
import threading
def ssh2(ip,username,passwd,cmd):
    try:
        paramiko.util.log_to_file('paramiko________.log')
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ip,22,username,passwd,timeout=5)
        for m in cmd:
            stdin,stdout,stderr = ssh.exec_command(m)
            #stdin.write("Y")   #简单交互，输入 ‘Y’
            out = stdout.readlines()
            # outerr = stderr.readlines()
            #屏幕输出
            for o in out:
                print (o)
            print ('%s  %s\tOK\n'%(ip,m))
        ssh.close()
    except :
        print ('%s\tError\n'%(ip))

def ssh2_pithy(ip,username,passwd,cmd):
    try:
        paramiko.util.log_to_file('paramiko________.log')
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ip,22,username,passwd,timeout=5)
        
        stdin,stdout,stderr = ssh.exec_command(cmd)
        out = stdout.readlines()
        #屏幕输出
        print ('[%s@%s]#%s\n'%(username,ip,cmd))
        for o in out:
            print (o) 
        ssh.close()
    except :
        print ('%s\tError\n'%(ip))
    finally:
    	return 1


def download(ip, username, passwd, local_dir, remote_dir):
   try:
        paramiko.util.log_to_file('paramiko_download.log')
        t = paramiko.Transport((ip,22))
        t.connect(username=username,password=passwd)
        sftp = paramiko.SFTPClient.from_transport(t)
        files = sftp.listdir(remote_dir)


        for f in files:
            print ('')
            print ('############################')
            print ('Beginning to download file  from %s  %s ' % (ip, datetime.datetime.now()))
            print ('Downloading file:', os.path.join(remote_dir, f))
            sftp.get(os.path.join(remote_dir, f), os.path.join(local_dir, f))#下载
            print ('Download file success %s ' % datetime.datetime.now())
            print ('')
            print ('############################')
        t.close()
   except:
        print ("connect error!")


def upload(ip, username, passwd, local_dir, remote_dir):
    try:
        paramiko.util.log_to_file('paramiko_upload.log')
        t = paramiko.Transport((ip, 22))
        t.connect(username=username, password=passwd)
        sftp = paramiko.SFTPClient.from_transport(t)
        #files = sftp.listdir(remote_dir)
        files = os.listdir(local_dir)
        for f in files:
            print ('')
            print ('############################')
            print ('Beginning to upload file  to %s  %s ' % (ip, datetime.datetime.now()))
            print ('Uploading file:', os.path.join(local_dir, f))
            sftp.put(os.path.join(local_dir, f), os.path.join(remote_dir, f))#上传
            print ('Upload file success %s ' % datetime.datetime.now())
            print ('')
            print ('############################')
        t.close()
    except:
        print ("connect error!")
        print (ip, "fail!")


if __name__=='__main__':

    a=threading.Thread(target=ssh2,args=('10.0.0.88','root','123456',['mkdir /root/look_at_this/','ls']))
    a.start()
        
    a=threading.Thread(target=upload,args=('10.0.0.88','root','123456','D:\\python-learn\\test_upload','/tmp/upload/'))
    a.start()
    
    a=threading.Thread(target=download,args=('10.0.0.88','root','123456','D:\\python-learn\\test_upload','/root/look_at_this/'))
    a.start()
   