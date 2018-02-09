import socket

def newServer(port):
    BUFFER_SIZE= 500
    serverHandle = "Eli's server> "

    TCP_PORT = port
    TCP_IP = '127.0.0.1'

    serverSocket = socket.socket()
    serverSocket.bind((TCP_IP, TCP_PORT))

    print "socket bound to port: " + str(TCP_PORT)
    serverSocket.listen(1)
    print "socket is waiting for connections"
    while True:
        connect, address = serverSocket.accept()
        #1st message is going to be username
        print "Incoming connection: {} : {}".format(address[0], address[1])
        data = ""
        while True:
            data = connect.recv(BUFFER_SIZE)
            if "CLIENT IS QUITTING" in data:
                print "Client has terminated session"
                print "Returned to listening"
                connect.close()
                break

            print "FROM: " + data
            # message = raw_input("TO: ")
            # if "/quit" in message:
            #     connect.send("Server is terminating connection")
            #     print "ending connection"
            #     connect.close()
            #     break
            connect.send(serverHandle + "RECEIVED")

    connect.shutdown(socket.SHUT_RDWR)
    connect.close()

newServer(16014)