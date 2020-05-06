# import socket module

from socket import *

serverSocket = socket(AF_INET, SOCK_STREAM)

# Prepare a server socket
# Fill in start
serverSocket.bind(('', 81))  # 使用 81 端口
serverSocket.listen(1)
# Fill in end

while True:
    # Establish the connection
    print('Ready to server...')
    # Fill in start
    connectionSocket, addr = serverSocket.accept()
    # FIll in end
    try:
        # Fill in  start
        # receive bytes from Client
        # it should decode to UTF-8
        message = connectionSocket.recv(1024)
        print('Get message:\n{}'.format(message))
        # Fill in end
        """
        GET /somedir/page.html HTTP/1.1
        Host: xxx
        Connection: xxx
        """
        filename = message.split()[1]
        f = open(filename[1:])
        # Fill in start
        outputdata = f.read()
        header = 'HTTP/1.1 200 OK \nConnection: close\n' + \
                 'Content0Length: {}\n'.format(len(outputdata)) + \
                 'Content-Type: text/html\n\n'
        connectionSocket.send(header.encode())
        # Fill in end
        # Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.close()
    except IOError:
        # Send response message for file not found
        # Fill in start
        header = 'HTTP/1.1 404 Not Found'
        connectionSocket.send(header.encode())
        # Fill in end
        # Close client socket
        # Fill in start
        connectionSocket.close()
        # Fill in end
serverSocket.close()
