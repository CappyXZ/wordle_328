###########################################################################################
# Ben Miller, Cade Fandl, Gabe Sullivan
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
# How to run: python client.py < host name > [ port number ]
###########################################################################################

# imports
import socket
import sys
import wordleLib as lib

# Function name: wordle_game 
# Description: This function will perform the wordle game
# it will check guesses, give feedback, show unguessed letters,
# show correct and letters in the wrong place.
# Parameters (input): string hidden_word - the hidden word sent by the server
def wordle_game(hidden_word):
    attempts = 6
    word_len = 5
    feedback = ""
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    guessed_letters = set()
    correct_letters = set()
    sorta_correct_letters = set()

    already_guessed = []
    prev_feedback = []

    #print out the games rules and how it will work
    print("New game started 6 attempts, the hidden word is 5 characters long")
    print("The symbol ""@"" means the letter is in the word but in the wrong place")
    print("The symbol ""#"" means the letter is not in the word")
    print("The guess must be 5 characters exactly")
    while attempts > 0:
        print(f"{attempts} attempts left:")
        guess = input("Input guess here: ").lower()
        if len(guess) != word_len:
            print("The guess must be 5 characters exact")
            continue
        # if the guess was previously guessed give the user a retry
        elif guess in already_guessed:
            print("Please guess a new word")
            continue
        
        #add all the characters in the guess to the guessed_letters set
        guessed_letters.update(guess)

        #add the guess to a list which contains all previously guessed words
        already_guessed.append(guess)

        # if the user wins
        if guess == hidden_word:
            print("You Won!!!")
            print(f"With {attempts} remaining!!!")
            break

        else:
            for i in range(len(hidden_word)):
                hidden_char = hidden_word[i]
                guess_char = guess[i]
                if guess_char == hidden_char: # see if the char is in the correct spot
                    feedback += guess_char
                    correct_letters.add(guess_char)
                elif guess_char in hidden_word: # see if the char is in the word but in the wrong spot
                    feedback += "@"
                    sorta_correct_letters.add(guess_char)
                else: # not in the word
                    feedback +="#"

            # difference_update & sets citation            
            #https://www.w3schools.com/python/ref_set_difference_update.asp
            #https://www.w3schools.com/python/python_sets_methods.asp
            # will make sure a letter does not appear in both sorta_correct_letters and correct_letters
            # correct_letters takes priority so the letter will stay in that set but not the other
            sorta_correct_letters.difference_update(correct_letters)

            #stores previous feedback for gameplay quality for user (less scrolling up & down)
            prev_feedback.append(feedback)

            #reset unguessed_letters every loop to make sure there is no duplicate letters
            unguessed_letters = []

            # checks if each character in the alphabet was 
            # previously guessed this round then will add it to the unguessed letters list.
            for char in alphabet:
                if char not in guessed_letters:
                    unguessed_letters.append(char)

            print("The symbol ""@"" means the letter is in the word but in the wrong place")
            print("The symbol ""#"" means the letter is not in the word")
            print(f"Guess: {guess}") 
            print(f"Hint:  {feedback}") 
            print(f"Previous hints: {prev_feedback}")
            print(f"Correct Letters: {correct_letters}")
            print(f"In word but wrong place letters: {sorta_correct_letters}")
            print(f"Unguessed Letters: {unguessed_letters}")

            #reset feedback
            feedback = ""
            # decrement attempts
            attempts -= 1

    # check to see if player lost
    if attempts == 0:
        print("All 6 attempts used!")
        print(f"Hidden word was: {hidden_word}")
        print("You lost!!!")




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
        port = 13367

    # Create a TCP/IP socket
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Connect the socket to the server
        s.connect((host, port))
        print(f"Connected to server at {host}:{port}")
        #recieve message
        msg1 = lib.recv_msg(s)
        if msg1 == "HELLO":
            #send message telling server the it is ready for a hidden word
            lib.send_msg("READY", s)
            while 1:
                hidden_word = lib.recv_msg(s)
                #start the game
                wordle_game(hidden_word)
                user_input = input("Would you like to play again? [y/n]: ").lower()
                while user_input != "y" and user_input != "n":
                        user_input = input("Input must be [y/n]: ").lower()
                # tell server the user still wants to play and request a new word
                if user_input == "y":
                    lib.send_msg("READY", s)
                #if user no longer wants to play tell server and disconnect
                elif user_input == "n":
                    lib.send_msg("BYE", s)
                    break
    except KeyboardInterrupt:
            lib.send_msg("BYE", s)
    except OSError as error:
        print(f"Socket error: {error}")
    finally:
        s.close()




if __name__ == "__main__":
    main()