import socket 

host = "192.168.1.136"
port = 9999
terminate = ["Bye","bye",""]

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server.bind((host,port))

server.listen(5)

while True:
    try:
        message = "a"
        client_socket,addr = server.accept()
        print(f"Received connection form {addr[0]} with port {addr[1]}")
        
        while message not in terminate :
            message = client_socket.recv(1024)
            message = message.decode('utf-8')
            print(f"The client says: {message}")

            responseMessage = input("Enter message:  ")
            client_socket.send(responseMessage.encode('utf-8'))  
            if responseMessage in terminate:
                break
            
        break  

    except:
        break
print("Connection Terminated!!")
client_socket.close()
