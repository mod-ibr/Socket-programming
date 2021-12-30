#socket library and time and json
import socket, time ,json

PERIOD = 0.5
SERVER = "192.168.1.11"
PORT   = 8888

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#connect this socket to the server(192.168.1.11).

s.connect((SERVER,PORT))

while True:
    try: 
        
        #msg to be sent
        msg = {"MSG":"This Dictionary is Sent as a json to the host through the Socket...!", 
               "CLIENT": "Client_1"}

        msgJSON = json.dumps(msg)
        #send request.
        s.sendall(bytes(msgJSON,'utf-8'))

        #receive responses.
        data = s.recv(1024)

        #Handle responses.
        notificationReply = data.decode()

        #notification reply
        print(notificationReply)
        time.sleep(1)
    except Exception as ex:
        print("connection Error")
        time.sleep(2)
        continue
    time.sleep(.3)
    
#close the Socket.
s.close()
