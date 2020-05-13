# UDPPingerServer.py
# We will need the following module to generate randomized lost packets import random
import random
from socket import *

# Create a UDP socket
# Notice the use of SOCK_DGRAM for UDP packets
serverSocket = socket(AF_INET, SOCK_DGRAM)
# Assign IP address and port number to socket
serverSocket.bind(('', 12000))

sequence_number = 0
recieved_time = 0
timeThres = 2.0
serverSocket.settimeout(timeThres)

while True:
    try:
        # Generate random number in the range of 0 to 10
        rand = random.randint(0, 10)
        # Receive the client packet along with the address it is coming from
        message, address = serverSocket.recvfrom(1024)
        # Capitalize the message from the client
        message = message.upper()
        received_arry = message.decode().split(' ')
        received_seq = int(received_arry[1])
        recieved_time = float(received_arry[2])
        if received_seq != sequence_number + 1:
            if sequence_number != 0:
                for i in range(sequence_number + 1, received_seq):
                    print("Dropped Packet: {}".format(i))
            else:
                print("Client connect")
        sequence_number = received_seq
        print("Recieve: {}".format(message.decode()))
        # If rand is less is than 4, we consider the packet lost and do not respond
        if rand < 4:
            continue
            # Otherwise, the server responds
        serverSocket.sendto(message, address)
    except Exception as e:
        if sequence_number == 0:
            continue
        else:
            print('Client disconnect(timeout)')
            sequence_number = 0
            recieved_time = 0
            continue
serverSocket.close()