from socket import *

serverPort = 12001
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
"""
1 表示请求连接的最大数
至少为 1
"""
serverSocket.listen(1)
while True:
    # 创建新的套接字
    # 由发起请求的用户专用
    connectionSocket, addr = serverSocket.accept()
    sentence = connectionSocket.recv(1024).decode()
    capitalizedSentence = sentence.upper()
    connectionSocket.send(capitalizedSentence.encode())
    connectionSocket.close()
