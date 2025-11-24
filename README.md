# Team Details

Cade Fandl - Project Leader and server code
Ben Miller - client code
Gabriel Sullivan - library code and readme

# Project Description

This project contains a Wordle server, client, and library used for entertainment.
The client contacts the server for a word which the player then must guess.
The client will handle all of the guess checking and other gameplay methods. 
The server will be concurrent and will handle multiple clients at once using threads. 
The library will be used to store functions that will be the same between the server
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
