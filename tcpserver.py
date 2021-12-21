#socket_echo_server.py
import socket
import sys
#Create a tcpip socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '192.168.103.78'
port = 8080
server_address = (host, port)
sock.bind(server_address)
sock.listen(1)

print('starting up on  {} port {}'.format(*server_address))
while True:
    print('waiting for connection')
    connection, client_address = sock.accept()
    try:
        print('connection from',client_address)
        data = b'Login:'
        
        while True:
            data = connection.recv(128)
            print('received {!r}'.format(data.decode("utf-8")))
            if data:
                print('sending data to the client')
                connection.sendall(data)
                break
            else:
                print('no data from', client_address)
                break
    finally:
        connection.close()