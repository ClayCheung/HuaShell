def isIP(str1):
	tag = True
	str1 = str1.strip()
	section_num = len(str1.split('.'))  # section_num == 4
	if section_num != 4 :
		tag = False
		return tag

	try:
		for i in range(0,4):
			if int(str1.split('.')[i]) < 0 :
				tag = False
				break
			elif int(str1.split('.')[i]) > 255 :
				tag = False
				break
	except :
		tag = False
	finally:
		return tag


def isIPrange(str1):
	str1 = str1.strip()
	if isIP(str1.split(',')[0].split('-')[0]) :
		return True
	else:
		return False


def iprange_to_list(ip_range):
	ip_list = []
	ip_range = ip_range.strip()
	comma_section_num = len(ip_range.split(','))
	comma_section = ip_range.split(',')
	for i in range(0,comma_section_num):
		cur_comma_section = comma_section[i].strip()
		if len(cur_comma_section.split('-')) == 2:
			#有范围，eg: 192.168.1.1-100
			start_ip = cur_comma_section.split('-')[0]
			start_ip_d = int(start_ip.split('.')[3])
			end_ip_d = int(cur_comma_section.split('-')[1])
			ip_abc = start_ip.split('.')[0]+'.'+start_ip.split('.')[1]+'.'+start_ip.split('.')[2]
			for d in range(start_ip_d,end_ip_d+1):
				cur_ip = ip_abc+'.'+str(d)
				ip_list.append(cur_ip)

		elif len(cur_comma_section.split('-')) == 1:
			#单个IP
			ip_list.append(cur_comma_section)
		else:
			print('Error:IP_range输入格式不合规')
			return -1
	return ip_list






def ip_parse(str1):
	#输入的如果是IP range,则返回ip_list
	#输入的如果是文件，则返回文件中的ip_list
	ip_list = []
	str1 = str1.strip()
	if isIPrange(str1) :
		#输入的是ip range
		ip_list = iprange_to_list(str1)
		for host in ip_list:
			if not isIP(host):
				print('Error:IP_range输入格式不合规')
				return -1
		
	else :
		#输入的是文件路径
		with open(str1,'r') as f:
			hosts = f.readlines()
			for host in hosts:
				if isIP(host):
					host = host.strip('\n')
					ip_list.append(host)
				else:
					print('Error:'+str1+'文件中存在不合规ip')
					return -1
	return ip_list


if __name__=='__main__':
	'''
	ip = input('请输入测试IP：')
	print(isIP(ip))
	ip_r = input('请输入测试IP_range：')
	print(isIPrange(ip_r))
	
	ip_r = input('请输入测试IP_range：')
	print(iprange_to_list(ip_r))
	'''
	str1 = input('请输入测试IP_range或文件路径:')
	print(ip_parse(str1))