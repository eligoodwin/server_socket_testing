#!/usr/bin/python2
"""
    Program: chatServe
    Author: Eli Goodwin
    Date: 2018/02/06
    Description: this is s simple chat server that works in conjunction with another
        a chat client. Users can take turns to exchanging messages
    Operation:
        1. ./serverChat.py <portNumber>
        2. corresponding chat client must be running in another terminal window or on
            another machine
    """
import socket
import sys


def checkArgs():
    """
    Function: checkArgs()
    Description: checks incoming cmd line arguments and if the port number was provided
    Pre-Condition: must be ran first
    Post-Condition: none
    return: none
    """
    if len(sys.argv) < 2:
        print "To few arguments. Expected : python " + sys.argv[0] + " <portNumber> "
        sys.exit()


def sendMessage(message, connection):
    """
        Function: sendMessage
        Description: used to send a message to the chat client
        Paramaters: message = message to send, connection=connection object
        Pre-Condition:
            1. connection listener active
            2. client has connected to the server and sent a message
            3. connection to client must be active
        Post-Condition:
        return: none
    """
    serverHandle = "Eli's Server> "
    outMessage = serverHandle + message
    connection.send(outMessage)


def receiveMessage(connection):
    """
        Function: receiveMesssage
        Description: used to receive messages from client
        Parameters: connection=connection object
        Pre-Condition:
            1. connection listener active
            3. connection to client must be active
        Post-Condition: none
        return: message from cliemt
    """
    BUFFER_SIZE = 500
    data = connection.recv(BUFFER_SIZE)
    return data

def initServer(port):
    """
        Function: initServer
        Description: used to used to make the server
        Paramaters: port= port number to create
        Pre-Condition:
            port must be valid
        Post-Condition:
        return: serverSocket object
    """
    TCP_PORT = port
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serverSocket.bind(('',TCP_PORT))
    serverSocket.listen(1)

    return serverSocket



def newServer(port):
    """
        Function: newServer
        Description: usedt to init and drive the server for chatting with the client
        Paramaters: port = port to create connection listener on
        Pre-Condition:
            port number must be valid
        Post-Condition: none
        return: none
    """
    #welcoem message
    print "Welcome to the chat server. To use wait for a client to connect. Once connected" \
          "you can exchange messages with them. To stop chatting with client enter: '/quit'. " \
          "To exit type cntrl + c to terminate server"
    #make server
    serverSocket = initServer(port)
    print "Socket is waiting for connections"
    #wait for connection
    while True:
        connect, address = serverSocket.accept()
        #1st message is going to be username
        print "Incoming connection: {} : {}".format(address[0], address[1])

        #allow persistent connection
        while True:
            data = ""
            data = receiveMessage(connect)
            #if quit from client end session gracefully
            if "/quit" in data:
                print "Client has terminated session"
                print "Returned to listening"
                message = "BUH-BYE"
                sendMessage(message, connect)
                connect.close()
                break

            print "FROM: " + data
            message = raw_input("TO: ")
            #if response to client is quit end gracefully
            if "/quit" in message:
                sendMessage(message, connect)
                print "ending connection"
                print "Returned to listening"
                connect.close()
                break
            # send message from server to client
            sendMessage(message, connect)
        #close connection wait for new one
        connect.close()

#check args for valid inputs
checkArgs()
#init server with passed port number
newServer(int(sys.argv[1]))