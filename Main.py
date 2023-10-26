import socket

# client method
def client():
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

# server method
def server():
    # creates a socket object called socketObject with the socket family type and socket type listed as a parameter
    # socket.AF_INET is IPV4
    # socket.SOCK_STREAM is a TCP socket
    socketObject = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # this binds the socket object to a address and port number using the address and port number as a parameter
    # socket.gethostname gets the address of the local host or machine running the server
    # 6604 is the port number which can be anything but port numbers under 5000 is often used by bigger companies
    socketObject.bind((socket.gethostname(), 6604))

    # this socket object will now listen to any calls made to the address and port number with a parameter of the size of the queue
    # 10 means the queue size will be 10
    socketObject.listen(10)

    print("Server started")

    # this socket object will listen forever until the server is closed is ended
    while True:

        # when a client connects the socketObject will accept the connection and store the client's socket and address in clientsocket and address
        clientsocket, address = socketObject.accept()

        # prints in the cmd that a connection has been established with a user
        print(f"Connection with a client with the address {address} has been established!")

        clientsocket.send(bytes("Welcome to the ReverseEchoServer \nEnter a message: ", "utf-8"))

        while True:
            # gets the message that was sent to the server by the client and 1024 is the buffer size
            msg = clientsocket.recv(1024)

            print("----------------------------------")

            print(f"\nMessage Received from {address}:")
            # decodes the message that is in utf-8
            msgReverse = msg.decode("utf-8")
            print(msgReverse)
            print("----------------------------------")

            # reverses the message
            msgReverse = msgReverse[::-1]

            #if msg is end this means the user wants to end the program
            if msgReverse == 'dne':

                # reverses the message
                msgReverse =  "Message Reversed: " + msgReverse

                # sends the reverse message back to the client in utf-8
                clientsocket.send(bytes(msgReverse, "utf-8"))
                print("----------------------------------")
                print(f"Message Sent to {address}:")
                print(msgReverse)
                print("----------------------------------")
                print(f"Client {address} disconnected from the server")
                # exits the program
                break

            # reverses the message
            msgReverse =  "Message Reversed: " + msgReverse + "\nEnter a message(type 'end' to stop the Echo Server): "

            # sends the reverse message back to the client in utf-8
            clientsocket.send(bytes(msgReverse, "utf-8"))
            print("----------------------------------")
            print(f"Message Sent to {address}:")
            print(msgReverse)
            print("----------------------------------")


# execution code
choice = input("Are you the server or client")

if choice == "server":
    server()
elif choice == "client":
    client()