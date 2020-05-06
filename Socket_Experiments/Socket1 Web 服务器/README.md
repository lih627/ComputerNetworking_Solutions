# 作业 1: WebServer

# 代码框架

题目给定的代码如下

```python
# import socket module

from socket import *

serverSocket = socket(AF_INET, SOCK_STREAM)

# Prepare a server socket
# Fill in start
# Fill in end

while True:
    # Establish the connection
    print('Ready to server...')
    # Fill in start
    connectionSocket, addr =
    # FIll in end
    try:
        # Fill in  start
        message =
        # Fill in end
        filename = message.split()[1]
        f = open(filename[1:])
        # Fill in start
        outputdata =
        # Fill in end
        # Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i])
        connectionSocket.close()
    except IOError:
        # Send response message for file not found
        # Fill in start
        # Fill in end
        # Close client socket
        # Fill in start
        # Fill in end
```



# 作业要求

1. 建立 socket, bind, send, receive HTTP packet
2. 服务器每次处理一个 HTTP 请求, 需要接受并解析 HTTP 请求. 请求的文件在服务器文件系统中. 需要构造相应, 包括请求的文件. 送到客户端, 如果文件不存在, 报 404

**提高**

1. multithreaded server 同时处理多个请求

   1. main thread 用来监听固定的端口
   2. 接受 TCP 请求创建子线程, 子线程用于交互

2. 写一个 HTTP 客户端测试服务器, 客户端可以通过 command line 指定服务器 IP 和端口号,如下所示

   ```bash
   client.py server_host server_port filename
   ```





# 完成版本 1

完成普通要求

`WebServer.py`

```python
#import socket module
from socket import *
serverSocket = socket(AF_INET, SOCK_STREAM) 
#Prepare a sever socket 
serverSocket.bind(('', 6789)) # 将TCP欢迎套接字绑定到指定端口
serverSocket.listen(1) # 最大连接数为1

while True:
	#Establish the connection
	print('Ready to serve...')
	connectionSocket, addr = serverSocket.accept() # 接收到客户连接请求后，建立新的TCP连接套接字
	try:
		message = connectionSocket.recv(1024) # 获取客户发送的报文
		filename = message.split()[1]
		f = open(filename[1:])
		outputdata = f.read(); 
		#Send one HTTP header line into socket
		header = ' HTTP/1.1 200 OK\nConnection: close\nContent-Type: text/html\nContent-Length: %d\n\n' % (len(outputdata))
		connectionSocket.send(header.encode())

		#Send the content of the requested file to the client
		for i in range(0, len(outputdata)):
			connectionSocket.send(outputdata[i].encode())
		connectionSocket.close()
	except IOError:
		#Send response message for file not found
		header = ' HTTP/1.1 404 Not Found'
		connectionSocket.send(header.encode())
		
		#Close client socket
		connectionSocket.close()
serverSocket.close()
```



# 提高版本 2

通过 `MultiThreading`实现并发

参考[GeekforGeeks: Sockets and MultiThreading](https://www.geeksforgeeks.org/socket-programming-multi-threading-python/)

代码如下, 我去掉了关于上锁和释放锁的部分. 因为不涉及共享内存的读取

但是不清楚这样做是否会出现问题.



```python
# import socket module

from socket import *
from _thread import *
import threading

print_lock = threading.Lock()


def threaded(c):
    try:
        message = c.recv(1024)
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = f.read()
        header = 'HTTP/1.1 200 OK \nConnection: close\n' + \
                 'Content0Length: {}\n'.format(len(outputdata)) + \
                 'Content-Type: text/html\n\n'
        c.send(header.encode())
        for i in range(0, len(outputdata)):
            c.send(outputdata[i].encode())
        c.close()
    except IOError:
        header = 'HTTP/1.1 404 Not Found'
        c.send(header.encode())
        c.close()


def main():
    serverSocket = socket(AF_INET, SOCK_STREAM)

    # Prepare a server socket
    # Fill in start
    serverSocket.bind(('', 81))  # 使用 81 端口
    serverSocket.listen(1)
    # Fill in end

    while True:
        try:
            # Establish the connection
            print('Ready to server...')
            # Fill in start
            connectionSocket, addr = serverSocket.accept()
            # FIll in end
            start_new_thread(threaded, (connectionSocket,))
        except:
            print('Exit')

            break
    # 关闭服务端
    serverSocket.close()


if __name__ == '__main__':
    main()

```

