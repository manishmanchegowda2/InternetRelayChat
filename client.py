#Portland State University
#Professor Nirupama Bulusu
#IRC Project

import threading
import socket
import sys

nickname = input("Enter your name: ")
threads = []
#To start the connection
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 55555))

#to recieve and send message from the server
def receive():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            if message == 'NICK':
                client.send(nickname.encode('utf-8'))
            elif message == 'QUIT':
                sys.exit(2)
            else:
                print(message)
        except Exception as e:
            print('Server not responding')
            client.close()
            sys.exit(2)

def write():
    while True:
        message = '{} {}'.format(nickname, input(''))
        try:
            client.send(message.encode('utf-8'))
        except:
            sys.exit(0)

receive_thread = threading.Thread(target=receive)
receive_thread.start()
threads.append(receive_thread)
write_thread = threading.Thread(target=write)
write_thread.start()
threads.append(write_thread)
