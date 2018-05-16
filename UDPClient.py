from socket import *
serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM) # 1st means IPv4, 2nd means UDP
message =  raw_input('Input lowercase sentence:')
clientSocket.sendto(message, (serverName, serverPort))
modifiedMessage, serverAddress = clientSocket.recvfrom(2048) # 2048 is buf size
print(modifiedMessage)
clientSocket.close()
from IPython import embed; embed();
