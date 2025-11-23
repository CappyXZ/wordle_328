###########################################################################################
# Ben Miller, Cade Fandl, Gabe Sullivan
# Computer Science
# Created: November 14, 2025
# Due: November 24, 2025
# CSC 328
# Prof Reiley Walther
# Group Assignment - Wordle
# server.py
# Purpose: This is the server program for a networked version of Wordle. It takes multiple
# connections at once using threads and will send a random word to the client.
# Language: Python
# How to run: python server.py [ port number ]
###########################################################################################


import socket as sock
import random
import sys
import threading
import wordleLib as lib

# word bank to send a word to user
word_bank = ["crane","sloth","brick","ghost","plant","sharp","flame","crown","vigor","joint",
             "sting","patch","blimp","draft","hound","grasp","piano","truck","flock","trace"]


# Function name: usage 
# Description: This function will make sure the user runs the program correctly 
# and print the usage clause if it was ran incorrectly.
# Parameters (input): N/A
# Return Value: none
def usage():
    if len(sys.argv) == 1:
        port = 13367
    elif len(sys.argv) == 2:
        port = int(sys.argv[1])
        
        if port > 65000 or port < 1024:
            print("Please enter a port number between 1024 and 65000") 
            sys.exit()
    else:
        print(f"Usage:, {sys.argv[0]}: [port number]")
        sys.exit()
    return port

# Function name: client_work 
# Description: This function will communicate with a single client which it will do in a thread
# to ensure concurrency. 
# Parameters (input): client_sock - client socket file descriptor
#                     client_addr - the client's address
# Return Value: none
def client_work(client_sock, client_addr):
    try:
        print(f'Connect by {client_addr}')
        lib.send_msg("HELLO", client_sock)
        while 1:  
            msg2 = lib.recv_msg(client_sock)
            if msg2 == "READY" or msg2 == "WORD":
                random_word = random.choice(word_bank)
                lib.send_msg(random_word, client_sock)
                print(f"The random word is: {random_word}")
            elif msg2 == "BYE" or msg2 == "QUIT":
                break
    finally:
        client_sock.close()
        print(f"Closed connection: {client_addr}")




def main():
    # make sure program is ran correctly
    port = usage() 
    host = ''
    threads = []
    is_open = False
    try:
        #citation for this code block
        #https://stackoverflow.com/questions/19196105/how-to-check-if-a-network-port-is-open
        while is_open == False:
            test = sock.socket(sock.AF_INET, sock.SOCK_STREAM)
            rv = test.connect_ex((host, port))

            if rv == 0:
                print(f"Port {port} is used")
                port += 1
            else:
                print(f"Port {port} is not used")
                is_open = True
        test.close()

        
        serverAddr = (host, port)
        
        # create server socket
        server = sock.socket(sock.AF_INET, sock.SOCK_STREAM)
        # make it so the socket can reuse port quickly
        server.setsockopt(sock.SOL_SOCKET, sock.SO_REUSEADDR, 1) 
        # bind the server to server address
        server.bind(serverAddr)
        # listen for connections and hold a queue up to 5 connections
        server.listen(5)
        print(f'Listening on {port}')
        while 1:
            #accept connection from client
            client_sock, client_addr = server.accept()
            #create a thread for a client
            client_thread = threading.Thread(target=client_work, args=(client_sock, client_addr))
            #add client to a list for easy cleanup
            threads.append(client_thread)
            #start the thread's work
            client_thread.start()
            if KeyboardInterrupt == True:
                break
    #error checking
    except OSError as error:
        print(f"Socket error: {error}")
    #ctrl c closes server safely
    except KeyboardInterrupt:
            server.close()
    finally:
        #close server
        server.close()
        #join all threads created
        for i in threads:
            i.join()
        print("")
        print("Server and all threads closed")


if __name__ == "__main__":
    main()

