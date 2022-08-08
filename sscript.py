# This is a mini project for  small chat box in a firm (06-06-2021)
# It consists of the server-side and the client side
# the server side  script will be run on the command line whiles the client script will be executed 
# with ip address, clients or workers can connect to the server through a local network

#---------------this scrit is the server script to be run on window cmd or terminal on linux-------------------------

import os
import socket
import threading
import time
import pathlib

hostname    = socket.gethostname()                                 # this is to get the system name
hostaddress = socket.gethostbyname(hostname)

HOST=hostaddress                                                   # port for the commumication
PORT=4545

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)             # creating a tcp socket with  the name soc
sock.bind((HOST,PORT))

clients=[] # creating clients ip list
names=[] # creating clients name list

def box():                     

    sock.listen(1000)                          # listening for connections
    print('sever is listening %s on port %s'%(HOST,PORT))

    while True:

        conn,addr= sock.accept()                # changing the socket module to accept new 
        name=conn.recv(8192000).decode('utf-8')   # receiving the name of the fresh client
        names.append(f"⏹{name}      ")              # stroing the name into the name list
        clients.append(conn)                   # stroing their ip address into clients list

        print(f'{name} has joined chat')

        sending(f"{name} has joined the chat ".encode('utf-8'))

        th=threading.Thread(target=incoming,args=(conn,addr))
        th.start()
        
        print(f'n# connections = {threading.activeCount()-1}')
        


def incoming(conn,addr):

    print(f'{addr} is connected')
    while True:
        message=conn.recv(8192000)   
        sending(message)
        sendnames(names)                         
          
    conn.close()

def sending(message):
    for i in clients:                 
        i.send(message)                            # sending received message to everyone on the client list

def sendnames(names):
    j=0
    for i in clients:
        while j<len(names):
            i.send(names[j].encode('utf-8'))
            j=j+1    

        
box()    # calling box               

    
    
    

        
       
        

