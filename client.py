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
#          to a server, checks user guesses, and gives feedback on those guesses.
# Language: Python
# How to compile: python client.py < host name > [ port number ]
###########################################################################################

# imports
import socket
import sys
import wordleLib as lib

def wordle_game(hidden_word):
    attempts = 6
    word_len = 5
    feedback = ""

    #print out the games rules and how it will work
    print("New game started 6 attempts, the hidden word is 5 characters long")
    print("The symbol ""!"" means the letter is in the correct place")
    print("The symbol ""@"" means the letter is in the word but in the wrong place")
    print("The symbol ""#"" means the letter is not in the word")
    while attempts > 0:
        print(f"{attempts} attempts left:")
        guess = input("Input guess here: ").lower()
        if len(guess) != word_len:
            print("The guess must be 5 characters exact")
            continue

        if guess == hidden_word:
            print("You Won!!!")
            break
        else:
            for i in range(len(hidden_word)):
                hidden_char = hidden_word[i]
                guess_char = guess[i]
                if guess_char == hidden_char:
                    feedback += "!"
                elif guess_char in hidden_word:
                    feedback += "@"
                else: 
                    feedback +="#"
            print(f"Guess: {guess}")
            print(f"hint:  {feedback}")
            feedback = ""
            attempts -= 1

    if attempts == 0:
        print("You lost!!! LOSER!!!!")




def main():
    msg_size = 512
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
        port = 13367

    # Create a TCP/IP socket
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Connect the socket to the server
        s.connect((host, port))
        print(f"Connected to server at {host}:{port}")
        msg1 = lib.recv_msg(s)
        if msg1 == "HELLO":
            lib.send_msg("READY", s)
            while 1:
                hidden_word = lib.recv_msg(s)
                wordle_game(hidden_word)
                user_input = input("Would you like to play again? [y/n]: ").lower()
                while user_input != "y" and user_input != "n":
                        user_input = input("Input must be [y/n]: ").lower()
                if user_input == "y":
                    lib.send_msg("READY", s)
                elif user_input == "n":
                    lib.send_msg("BYE", s)
                    break


    except OSError as error:
        print(f"Socket error: {error}")
    finally:
        s.close()




if __name__ == "__main__":
    main()