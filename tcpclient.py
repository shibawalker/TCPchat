#socket_echo_client.py
import socket
import sys
#Create a tcpip socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('127.0.0.1', 8080)
print('starting up on  {} port {}'.format(*server_address))

sock.connect(server_address)

try:
    #send data
    message = b'hello!'
    print('sending{!r}'.format(message.decode("utf-8")))
    sock.sendall(message)

    #look for resp
    amount_received = 0
    amount_expected = len(message)
    
    while amount_received<amount_expected:
        data = sock.recv(128)
        amount_received += len(data)
        print('received {!r}'.format(data.decode("utf-8")))
        
finally:
    print('closing socket')
    sock.close()