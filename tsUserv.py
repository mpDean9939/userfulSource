#!/usr/bin/env python

# -*- coding:utf-8 -*-

from socket import *
from time import ctime

HOST = ''
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST,PORT)

udpSerSock = socket(AF_INET,SOCK_DGRAM)#SOCK_DGRAM表示数据报类型，即UDP
udpSerSock.bind(ADDR)#绑定套接字

while True:
	print('waiting for message...')
	data,addr = udpSerSock.recvfrom(BUFSIZ)
	udpSerSock.sendto(('[%s] %s' %(ctime(),data)).encode('utf-8'),addr)#对收到的data数据进行utf-8编码，这是3.x针对2.x的改进，客户端做同样的处理
	print('...received from and returned to:',addr)

udpSerSock.close()