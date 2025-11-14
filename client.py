###########################################################################################
# Ben Miller, Cade Fandle, Gabe Sullivan
# Computer Science
# Created: November 14, 2025
# Due: November 24, 2025
# CSC 328
# Prof Reiley Walther
# Group Assignment - Wordle
# client.py
# Purpose: This is the client program for a networked version of Wordle. It connects 
#          to a server, sends user guesses, and receives feedback on those guesses.
# Language: Python
# How to compile: python client.py < host name > < port number >
###########################################################################################

# imports
import socket
import sys

def main():
    # error checking and usage clause
    if not (2 <= len(sys.argv) <= 3):
        print("Usage: python client.py <host name> [port number]")
        sys.exit(1)

    host = sys.argv[1]
    if len(sys.argv) == 3:
        try:
            port = int(sys.argv[2])
        except ValueError:
            print("Invalid port number. Port must be an integer.")
            sys.exit(1)
    else:
        port = 1337

    # Create a TCP/IP socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        # Connect the socket to the server
        sock.connect((host, port))
        print(f"Connected to server at {host}:{port}")

        while True:
            # Get user input
            guess = input("Enter your guess (or 'exit' to quit): ")
            if guess.lower() == 'exit':
                print("Exiting the game.")
                break

            # Send the guess to the server
            sock.sendall(guess.encode())

            # Receive feedback from the server
            feedback = sock.recv(1024).decode()
            print(f"Feedback from server: {feedback}")



if __name__ == "__main__":
    main()