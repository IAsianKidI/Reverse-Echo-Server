import socket

# gets the address of the server if local is typed it will use the local machines address
getAddress = input("Enter an Address to connect to.(If the local host type 'local'): ")
getMessage = "Hello"

# creates a socket object called sendSocketObject with the socket family type and socket type listed as a parameter
# socket.AF_INET is IPV4
# socket.SOCK_STREAM is a TCP socket
clientSocketObject = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# creates the connection using the local machines address or user inputs
if getAddress == 'local':
    clientSocketObject.connect((socket.gethostname(), 6604))
    getAddress = socket.gethostname()
    print("connected to local host")
else:
    clientSocketObject.connect((getAddress, 6604))
    print(f"connected to host {getAddress}")

# this socket object will listen forever until the server is closed is ended
while True:

    msg = clientSocketObject.recv(1024)

    print(f"\n--------------------------------\nMessage sent by server {getAddress}:\n--------------------------------")
    
    # prints the decoded msg sent by the server
    print(msg.decode("utf-8"))

    print("--------------------------------")

    if msg.decode("utf-8") == "Message Reversed: dne":
        print("Disconnected from server")
        exit()
        
    # gets the message is to be sent to
    getMessage = input()

    # sends it to the server
    clientSocketObject.send(bytes(getMessage, "utf-8"))


    
