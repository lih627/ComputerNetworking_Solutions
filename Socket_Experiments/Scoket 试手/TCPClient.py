from socket import *

serverName = '192.168.50.217' # Server IP
serverPort = 12001
"""
STREAM 指定 TCP 套接字类型
"""
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
sentence = input('Input lowercase sentence:')
# 建立好链接后不需要显示创建分组并分配端点地址
clientSocket.send(sentence.encode())
modifiedSentence = clientSocket.recv(2048)
print(modifiedSentence.decode())
clientSocket.close()
