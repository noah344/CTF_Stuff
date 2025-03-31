'''
CHRONOHACK
----------
This one was kinda cool, got to use pwntools more.
Pretty basic python looping logic.  EPOCH time is super precise, but not all computers
keep the same level of preciseness.  I had pwntools loop over and over
gradually increasing the time until I got the flag.  Pretty easy!  Didn't bother to do a writeup because...reasons.
'''
from pwn import *
import random
import time
# Initiates a string to hold the alphabet and sets up a string to set the start time.
alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
start = 0
port = int(input("Please enter the port: "))

while True:
    # Gets the current time and mirrors the level of preciseness set up on the token generation script that comes with the challenge.
    tim = int(time.time() * 1000) + start
    # Initializes a function to hold all of the strings we're going to try since we get 50 tries before it fails.
    strings = []

    # The remote server could have a current time more OR less than our current time, and since we get 50 tries we can do 25 less and 25 more than our current time.
    # For each value, it will use the current time + the value to set the seed for python's random function.
    # Then it will randomly pick 20 characters from the alphabet above and place them in a string before appending it to the list above.
    for i in range(-25,25):
        s = ""
        random.seed(tim + i)
        for j in range(20):
            s += random.choice(alphabet)
        strings.append(s)

    # Connects to the remote server.
    p = remote("verbal-sleep.picoctf.net", port)
    # Receives data until it gets to the text 'or exit):'
    p.recvuntil('or exit):')

    # Sends each line in our list
    for i in strings:
        p.sendline(i)

    # If the output contains the string 'congrat', we've successfully gotten the flag.
    res = p.clean().decode('latin-1')
    if "Congrat" in res:
        print(res)
        p.close()
        break
    # If it doesn't, we increase start by 20 and start all over.
    else:
        p.close()
        start = start + 20
