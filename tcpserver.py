#socket_echo_server.py
import socket
import sys
#Create a tcpop socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('192.168.217.78', 10000)
print('starting up on  {} port {}'.format(*server_address))
sock.bind(server_address)

sock.listen(1)

while True:
    print('waiting for connection')
    connection, client_address = sock.accept()
    try:
        print('connection from',client_address)

        while True:
            data = connection.recv(16)
            print('received {!r}'.format(data.decode("utf-8")))
            if data:
                print('sending data to the client')
                connection.sendall(data)
            else:
                print('no data from', client_address)
                break
    finally:
        connection.close()