import socket as sock
import sys
from wordleLib import getRandWord, getGuessResults

def usage():
    if len(sys.argv) == 1:
        port = 13367
    elif len(sys.argv) == 2:
        port = int(sys.argv[1])
        
        if port > 65000 or port < 1024:
            print("Please enter a port number between 1024 and 65000") 
            sys.exit()
    else:
        print(f"Usage:, {sys.argv[0]}: <tcp or udp>")
        sys.exit()
    return port
    



def main():
    port = usage()
    host = ''
    serverAddr = (host, port)
    msg_size = 512
    try:

        s = sock.socket(sock.AF_INET, sock.SOCK_STREAM)
        s.setsockopt(sock.SOL_SOCKET, sock.SO_REUSEADDR, 1)
        s.bind(serverAddr)
        s.listen(5)
        print(f'Listening on {port}')
        while 1:
            clientSock, addr = s.accept()
            print(f'Connect by {addr}')
            msg = clientSock.recv(msg_size)
            msg = msg.decode()
            print(f"Recieved {msg} from client")
            clientSock.send("Okay".encode())
            print("Said Okay")
            clientSock.close()
    except KeyboardInterrupt as key:
        s.close()

    finally:
        s.close()


        




if __name__ == "__main__":
    main()

