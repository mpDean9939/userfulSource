#!/usr/bin/env python

# -*- coding: utf-8 -*-

from socket import *
from time import ctime

HOST = ''#空表示blid函数可以绑定在所有有效的地址上
PORT = 21567#随便选的一个端口号，大于1024小于65535
BUFSIZ = 1024#缓冲区1k
ADDR = (HOST,PORT)

tcpSerSock = socket(AF_INET,SOCK_STREAM)#创建一个TCP/IP套接字
tcpSerSock.bind(ADDR)#绑定主机名到套接字，即把套接字绑定到服务器地址上
tcpSerSock.listen(5)#开始TCP监听，5表示最多允许5个连接同时连进来，而后来的连接就会被拒绝掉

while True:#无限循环
	print('waiting for connection...')
	tcpCliSock,addr = tcpSerSock.accept()
	print('...connection from:',addr)

	while True:
		data = tcpCliSock.recv(BUFSIZ)
		if not data:
			break
		tcpCliSock.send(('[%s] %s'%(ctime(), data)).encode('utf-8'))#收到消息后存在data里面再加个时间戳返回

	tcpCliSock.close()
tcpSerSock.close()#服务器一般不会关闭