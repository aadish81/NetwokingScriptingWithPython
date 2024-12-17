import socket 

host = "192.168.1.136"
port = 9999
terminate = ["Bye","bye",""]

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((host,port))

client.send("Hey There!!".encode('utf-8'))
while True:
    try:
        response = client.recv(1024)
        response = response.decode('utf-8')

        if response in terminate:
            break

        print(f"The server says: {response}")
        message = input("Enter message : ")
        client.send(message.encode('utf-8'))
        if message in terminate:
            break
        
    
    except:
        break

print("Connection Terminated!!")
client.close()
