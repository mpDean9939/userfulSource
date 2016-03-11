#!/usr/bin/env python

# -*- coding: utf-8 -*-

from socket import *

HOST = 'localhost'#表示服务器上的主机名和端口号，由于要在本机上测试，所以是localhost
PORT = 21567#端口号与服务器完全一致
BUFSIZ = 1024#缓冲区1k
ADDR = (HOST,PORT)

tcpCliSock = socket(AF_INET,SOCK_STREAM)#创建一个TCP/IP套接字
tcpCliSock.connect(ADDR)#绑定主机名到套接字，即把套接字绑定到服务器地址上

while True:
	data = input('> ')
	if not data:
		break
	tcpCliSock.send(data.encode('utf-8'))
	data = tcpCliSock.recv(BUFSIZ)
	if not data:
		break
	print (data)

tcpCliSock.close()