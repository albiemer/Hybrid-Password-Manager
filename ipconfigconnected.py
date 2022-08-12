#import socket

class myip:
    ip = '192.168.1.2'
    port = 5000

def fullip():
    return myip.ip + ':' + str(myip.port)

print(myip.ip)

"""def fullip(netlocal):
    if netlocal == 'yes':
        return myip.ipconnected + ':' + str(myip.port)
    else:
        return myip.ipoffline + ':' + str(myip.port)"""

