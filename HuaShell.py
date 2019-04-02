from py_ssh.ssh_py import ssh2,download,upload
import datetime
import os
import threading

opera= input('''
	* 首先请确保已经在 ./params文件夹中 填好了必要参数
	================================================
	================================================
	1.批量输入命令
	2.批量上传文件
	3.批量下载文件

	$你要执行什么操作（输入序号）:''')
if opera == '1':
	#cmd
	#读取账号、密码
	username = 'root'
	password = 'Passwd@root&2018'
	#读取命令
	cmds_f=open(".\\params\\cmds.txt")
	cmds=cmds_f.readlines()
	cmds_f.close()
    #读取服务器列表
	hosts_f=open(".\\params\\ip_list.txt")
	hosts=hosts_f.readlines()
	hosts_f.close()
	for host_ip in hosts:
		host_ip = host_ip.strip()
		a=threading.Thread(target=ssh2,args=(host_ip,username,password,cmds))
		a.start()

elif opera == '2':
	#upload
	dst_dir_path = input('请输入上传目的目录路径（直接回车默认上传至/tmp/）：')
	if dst_dir_path == '':
		dst_dir_path = '/tmp/'
	
	#读取账号、密码
	username = 'root'
	password = 'Passwd@root&2018'
	#读取上传文件所在文件夹路径
	upload_dir = '.\\upload_dir'
	#读取服务器列表
	hosts_f=open(".\\params\\ip_list.txt")
	hosts=hosts_f.readlines()
	hosts_f.close()

	for host_ip in hosts:
		host_ip = host_ip.strip()
	
		a=threading.Thread(target=upload,args=(host_ip,username,password,upload_dir,dst_dir_path))
		a.start()


elif opera =='3':
	#download
	print('友情提示：确保下载源的文件夹无嵌套文件夹，下载目的文件夹是空文件夹')
	print('-------------------------------------------------------------')
	src_dir_path = input('请输入下载源的路径文件夹（直接回车默认上传至/tmp/）：')
	if src_dir_path == '':
		src_dir_path = '/tmp/'
	#读取账号、密码
	username = 'root'
	password = 'Passwd@root&2018'
	#读取下载文件目的文件夹路径
	download_dir = '.\\download_dir'
	#读取服务器列表
	hosts_f=open(".\\params\\ip_list.txt")
	hosts=hosts_f.readlines()
	hosts_f.close()
	
	for host_ip in hosts:
		host_ip = host_ip.strip()

		a=threading.Thread(target=download,args=(host_ip,username,password,download_dir,src_dir_path))
		a.start()


else:
	print('请输入序号！')

input('')
