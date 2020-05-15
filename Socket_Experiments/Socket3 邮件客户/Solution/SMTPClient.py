import base64
from socket import *


def b64(strs):
    if not isinstance(strs, bytes):
        strs = strs.encode()
    ret = base64.b64encode(strs)
    return ret


def decodeb64(strs):
    if len(strs) != 2:
        for idx, val in enumerate(strs):
            if isinstance(val, bytes):
                strs[idx] = val.decode()
        return ' '.join(strs)
    if not isinstance(strs[1], bytes):
        strs[1] = strs[1].encode()
    strs[1] = base64.b64decode(strs[1]).decode()
    for idx, val in enumerate(strs):
        if isinstance(val, bytes):
            strs[idx] = val.decode()
    return ' '.join(strs)


msg = "\r\n I love computer networks!"
endmsg = "\r\n.\r\n"

# Choose a mail server (e.g. Google mail server) and call it mailserver
# Fill in start
# 选择 outlook STMP
# mailserver = 'smtp.office365.com'
mailserver = 'smtp.qq.com'
mailserverPort = 587
# Fill in end

# Create socket called clientSocket and establish a TCP connection with mailserver
# Fill in start
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((mailserver, mailserverPort))
# Fill in end

recv = clientSocket.recv(1024).decode()
print(recv)

# Send HELO command and print server response.
heloCommand = 'HELO Alice\r\n'
print('C: ' + heloCommand)
clientSocket.send(heloCommand.encode())
recv = clientSocket.recv(1024).decode()
print('S: ' + recv)

# Send MAIL FROM command and print server response.
# Fill in start
authCommand = 'AUTH LOGIN\r\n'
print('C: ' + authCommand)
clientSocket.send(authCommand.encode())
recv = clientSocket.recv(1024).split()
print('S: ' + decodeb64(recv))
# USERNAME AND PASSWORD
username = 'xxxxx@qq.com'
password = 'heajxxxxxxxxxxvbchc'
desitnation = 'xxxxxx@outlook.com'

print('C: Send UserName')
clientSocket.send(b64(username) + b'\r\n')
recv = clientSocket.recv(1024).decode().split()
recv = decodeb64(recv)
print('S: ' + recv)

print('C: Send PassWord')
clientSocket.send(b64(password) + b'\r\n')
recv = clientSocket.recv(1024).decode().split()
recv = decodeb64(recv)
print('S: ' + recv)

mfCommand = 'MAIL FROM: <{}>\r\n'.format(username)
print('C: MAIL FROM: <xxxxx@qq.com>')
clientSocket.send(mfCommand.encode())
recv = clientSocket.recv(1024).decode()
print('S: ' + recv)
# Fill in end

# Send RCPT TO command and print server response.
# Fill in start

rcptCommand = 'RCPT TO: <{}>\r\n'.format(desitnation)
print('C: RCPT TO: <xxxxx@outlook.com>')
clientSocket.send(rcptCommand.encode())
recv = clientSocket.recv(1024).decode()
print('S: ' + recv)

# Fill in end

# Send DATA command and print server response.
# Fill in start
print('C: DATA')
clientSocket.send('DATA\r\n'.encode())
recv = clientSocket.recv(1024).decode()
print('S: ' + recv)
# Fill in end

# Send message data.
# Fill in start
print('C: ' + msg)
clientSocket.send(msg.encode())
# Fill in end

# Message ends with a single period.
# Fill in start
print('C:' + endmsg)
clientSocket.send(endmsg.encode())
recv = clientSocket.recv(1024).decode()
print('S: ' + recv)
# Fill in end

# Send QUIT command and get server response.
# Fill in start
print('C: QUIT')
clientSocket.send('QUIT\r\n'.encode())
recv = clientSocket.recv(1024).decode()
print('S: ' + recv)
# Fill in end
clientSocket.close()
