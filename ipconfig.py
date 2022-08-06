#import socket

ip = '127.0.0.1'
    
port = 5000

def fullip():
    return ip + ':' + str(port)

#print(type(fullip()))