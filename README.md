# Team Details

Cade Fandl - Project Leader and server code
Ben Miller - client code
Gabriel Sullivan - library code and readme

# Project Description

This project is a Wordle game created using a server, client, and library used for entertainment. The client contacts the server for a word which the player then must guess.
The client will handle all of the guess checking and other gameplay aspects. 
The server will be concurrent and will handle multiple clients at once using threads. 
The library will be used to store functions that will both be used by the server
and client. 

# How to Compile

This project was done in python so there is no need for compiling

# How to Run the Client

usage:
python3 client.py <hostname> [port number]

How we ran it:
python3 client.py localhost

# How to Run the Server
usage:
python3 server.py [port number]

How we ran it:
python3 server.py

How to close server:
ctrl c once then wait for client to finish playing

# Library
static or shared?
We used a shared library because all imported .py files are automatically shared libraries.
They are loaded at runtime and are not compiled into our two programs.

# Known Issues
We noticed no issues throughout our testing process.

# How we worked as a team and identified the necessary tasks
We split up the work while also working together to make sure we had
a cohesive plan. We also updated eachother on progress via Discord.
To identify necessary tasks we mostly identified them as we worked. 
For example, we noticed in our testing that the previous guesses would
be hard to see during the gameplay printing out messages to the terminal.
To fix that we added a previous guesses list that held the player's previous
guesses and then printed them out with the other feedback. 
Another example is that we realized users could reguess the same word back to back
which didn't make any sense so we removed that by adding a new list holding previous guesses
and checked to see if the current guess was in that list. If it was it would allow the user
to input a new guess. 