import time
from socket import *

serverName = '192.168.50.217'
serverPort = 12000
timeoutValue = 1

clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.settimeout(timeoutValue)

for idx in range(10):
    sendTime = time.time()
    message = "Ping {} {}".format(idx + 1, sendTime)
    try:
        clientSocket.sendto(message.encode(), (serverName, serverPort))
        modifiedMessage, serverAddress = clientSocket.recvfrom(1024)
        rtt = time.time() - sendTime
        print('Sequence {}: Reply from {} RTT={:.4f}'.format(idx + 1,
                                                             serverName,
                                                             rtt))
    except Exception as e:
        print('Sequence {}: Requeset timed out'.format(idx + 1))
clientSocket.close()
