# Mod 26
This was a challenge listed in PicoCTF 2021.  It's listed as easy and categorized as a Cryptography challenge.

## Description
The Description reads:
> Cryptography can be easy, do you know what ROT13 is?  
> cvpbPGS{arkg_gvzr_V'yy_gel_2_ebhaqf_bs_ebg13_uJdSftmh}

## Hints
There is a single hint that reads:
> This can be solved online if you don't want to do it by hand!

# Solving
## My Thoughts
Super easy intro challenge to some cryptography concepts.

## Solution
With this challenge only being worth 10 points, it should be relatively easy.  With a lot of CTF challenges, there will be hints not only in the description, but also in the title.

So we have two things to look into based on the title and description, Mod 26 and ROT13.  A quick google search turns up a bunch of results for ROT13, I started with Wikipedia:  https://en.wikipedia.org/wiki/ROT13

ROT13 is a type of cryptographic cypher known as a simple substitution cypher that replaces a letter with the 13th letter after it in the alphabet.\
Well that's great, but we can see our flag has some non letter characters in it like 2 and ', not to mention capital letters.\

A really important note in the wikipedia article is this:
> Only those letters which occur in the English alphabet are affected; numbers, symbols, punctuation, whitespace, and all other characters are left unchanged. 

Ok so lets give this a try, we can use a simple table like the one below to make it a little easier:

Input\
ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz\
Output\
NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm

Original Text:  cvpbPGS{arkg_gvzr_V'yy_gel_2_ebhaqf_bs_ebg13_jdJBFOXJ}\
Decrypted Text:  picoCTF{next_time_I'll_try_2_rounds_of_rot13_wqWOSBKW}

Rather than do this by hand, let's use an awesome website called Cyberchef which should decode this entirely on it's own!

![Cyberchef](https://github.com/user-attachments/assets/4fbdbc78-c608-4e55-845e-69e1783e793a)

Tada!  I thought it would be good practice to write up a little script for this as well which you can find both in this subfolder and in the scripts folder at the root.  You can see the source below:

``` python
#! /usr/bin/python
# The above line just points Linux out to what program it should be using to run the script.

# argparse is just used to parse user arguments to tell the script what to do
import argparse
# os is used to determine if the file the user enters is valid.
import os

# Creates a main function where everything else is run from.
def main():
	# gets user arguments and validates them.
	args = get_args()
	
	# Checks if the user argument for file is set, if it is it'll call the parse_file function
	if args.file:
		parse_file(args.file)
	# if not it'll just call the decrypt function
	else:
		print(decrypt(args.text))

def get_args():
	"""Provides an argument parser to collect options fromt he user."""
	# initiates an argument parser object that will be responsible for parsing user input.
	parser = argparse.ArgumentParser(description="Takes in text or reads a file and decrypts ROT13 to human readable data.")
	# A mutually exclusive group will require the user to choose one and only one of the options from the group.
	# In our case we want the user to pick either a file or text.
	input_choice = parser.add_mutually_exclusive_group(required=True)
	
	# Initiates a few possible flags for the user to enter.
	input_choice.add_argument("-f", "--file", type=str, help="Provide the path to a file that contains at least one line of ROT13 encrypted text.", required=False)
	input_choice.add_argument("-t", "--text", type=str, help="Provide the single line of ROT13 encrypted text that you want to be decrypted.", required=False)

	# Parses the args into objects that we can use.
	args = parser.parse_args()
	
	# This just checks to make sure the file is valid if the user chose to enter a file.
	if args.file:
		if not os.path.isfile(args.file):
			print("The provided file is invalid, try again.")
			exit()

	# Returns the arguments to the main function.
	return parser.parse_args()

def parse_file(file):
	"""Reads through a file, gathers each line, and decrypts it before placing it back in a file."""
	# Opens the file the user entered.
	with open(file) as encfile:
		# Grabs each line and places it in a list.
		lines = encfile.read().splitlines()
	
	# Opens a file to place the decrypted text.
	with open("./decrypted.txt", "w") as decfile:
		# Loops through the encrypted lines and decrypts them one by one before writing them to the file.
		for i in lines:
			decfile.write(decrypt(i) + "\n")
			
def decrypt(line):
	"""Responsible for decrypting individual lines."""
	# These two strings are just used as indexes, the top one would be the rot13 encrypted character, the bottom would be the decrypted character.
	inp = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
	out = "NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm"
	
	# Initiates a string to hold our decryped line.
	dec_line = ""
	# Loops through each character in the line.
	for i in line:
		# Checks if the character is in the inp list above, meaning that this will only execute if it's a capital or lowercase letter in the english alphabet.
		if i in inp:
			# if it is, we get the index of the character in the inp string, and then get the corresponding character from the out string and append it to the dec_line string.
			dec_line = dec_line + out[inp.index(i)]
		else:
			# if not, we just add it to the dec_line string.
			dec_line = dec_line + i
	# Returns the dec_line string.
	return dec_line

# This is used to do stuff, it's complicated, look it up.
if __name__ == '__main__':
	main()
```
