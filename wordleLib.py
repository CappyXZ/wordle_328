###########################################################################################
# Ben Miller, Cade Fandl, Gabe Sullivan
# Computer Science
# Created: November 14, 2025
# Due: November 24, 2025
# CSC 328
# Prof Reiley Walther
# Group Assignment - Wordle
# wordleLib.py
# Purpose: This will be a shared library for our wordle game. It will hold the functions
# that both the server and client will use. 
# Language: Python
# How to compile: N/A
###########################################################################################

import socket as sock

msg_size = 512

# Function name: send_msg 
# Description: This function will make sure the user runs the program correctly 
# and print the usage clause if it was ran incorrectly.
# Parameters (input): string text - what the message will send to the recipient
#                     sock - the socket file descriptor
# Return Value: none
def send_msg(text, sock):
    msg = text.encode()
    sock.sendall(msg)

# Function name: recv_msg 
# Description: This function will recieve a message from a sender 
# and decode it.
# Parameters (input): sock - the socket file descriptor
# Return Value: string msg - the message recieved after being decoded
def recv_msg(sock):
    msg = sock.recv(msg_size)
    return msg.decode()
