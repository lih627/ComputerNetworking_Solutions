from socket import *

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
"""
bind((ADDRESS, PORT))
ADDRESS 不指定, 为了满足多个 IP 地址
"""
serverSocket.bind(('', serverPort))
print('The server is ready to receive')
while True:
    message, clientAddress = serverSocket.recvfrom(2048)
    print('Receive from: {}\n Message is: {}'.format(clientAddress, message.decode()))
    modifiedMessage = message.decode().upper()
    serverSocket.sendto(modifiedMessage.encode(), clientAddress)

