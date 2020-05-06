from socket import *

serverName = '192.168.50.217' # Server IP
serverPort = 12000  # 端口号
"""
AF_INET 指示底层网络使用 IPv4
SOCK_DGRAM 表示 UDP 套接字
"""
clientScoket = socket(AF_INET, SOCK_DGRAM)
message = input('Input lower case sentence: ')
clientScoket.sendto(message.encode(), (serverName, serverPort))
modifiedMessage, serverAddress = clientScoket.recvfrom(2048)  # 缓存长度 2048
print(modifiedMessage.decode())
clientScoket.close()
