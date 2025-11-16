import socket as sock
import random
import sys

#test
def usage():
    if len(sys.argv) == 1:
        port = 1337
    elif len(sys.argv) == 2:
        port = int(sys.argv[1])
        
        if port > 65000 or port < 1024:
            print("Please enter a port number between 1024 and 65000") 
            sys.exit()
    else:
        print(f"Usage:, {sys.argv[0]}: <tcp or udp> <hostname> ")
        sys.exit()
    return port
    



def main():
    port = usage()
    host = ''
    serverAddr = (host, port)
    s = sock.socket(sock.AF_INET, sock.SOCK_STREAM)
    s.bind(serverAddr)
    s.listen(5)
    print(f'Listening on {port}')
    while 1:
        clientSock, addr = s.accept()
        print(f'Connect by {addr}')


        




if __name__ == "__main__":
    main()

