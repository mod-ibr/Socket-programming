'''
Socket can be implementedby Queue and Threading.

This code is Server Socket as Queue 

'''
#importing all needed Lib
import socket, time,json

PERIOD = 1
PORT = 8888
MAX_QUEUE = 30
MAX_MSG_SIZE = 1024
SERVER = "192.168.1.11"

#create a socket as Server
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Bind the socket to range 8888 and accept any request from any client in the LAN
sock.bind((SERVER,PORT))

#Maximun Queue lenght (buffer size)
sock.listen(MAX_QUEUE)    

while True:
    
    #accept the connection
    connection , addressIP = sock.accept()
    
    try:
        while True:
            #Recisved data and saved to RecievedData and the maximun number of bytes is 1024
            recievedData = connection.recv(MAX_MSG_SIZE)
            
            #Any thing can be done as a request handle
            #the requset  is a Question
            #decoding data
            decodedData  = recievedData.decode()
            
            #get the original data from the JSON msg
            pureData = json.loads(decodedData)
            print(pureData)
            print(pureData["CLIENT"])
            print(pureData["MSG"])
    
            #Acknolage msg
            connection.sendall(b"From Host sent Succesfully")
    except Exception as ex:
        print(ex)
        if (not connection or not recievedData):
            break

#close connection
connection.close()
    
sock.close()