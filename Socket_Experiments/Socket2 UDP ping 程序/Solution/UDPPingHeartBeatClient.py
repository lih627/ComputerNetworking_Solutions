import time
from socket import *

serverName = '192.168.50.217'
serverPort = 12000
timeoutValue = 1
lostPacketCount = 0
RTTs = []
testLoopNumber = 20

clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.settimeout(timeoutValue)

for idx in range(testLoopNumber):
    sendTime = time.time()
    message = "Ping {} {}".format(idx + 1, sendTime)
    try:
        clientSocket.sendto(message.encode(), (serverName, serverPort))
        modifiedMessage, serverAddress = clientSocket.recvfrom(1024)
        rtt = time.time() - sendTime
        RTTs.append(rtt)
        print('Sequence {}: Reply from {} RTT={:.4f}'.format(idx + 1,
                                                             serverName,
                                                             rtt))
    except Exception as e:
        lostPacketCount += 1
        print('Sequence {}: Requeset timed out'.format(idx + 1))

print("RTT max:{:.4f}s min:{:.4f}s avg:{:.4f}".format(max(RTTs), min(RTTs), sum(RTTs) / len(RTTs)))
print("Packet Loss Rate: {:2f}".format(lostPacketCount / testLoopNumber * 100))

clientSocket.close()
