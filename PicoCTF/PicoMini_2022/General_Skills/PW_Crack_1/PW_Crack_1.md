# PW Crack 1
This was a challenge for PicoMini 2022.  It's listed as Easy and categorized as a General Skills challenge.  
Direct Link: https://play.picoctf.org/practice/challenge/245

## Description
The Description reads:
> Can you crack the password to get the flag?
> Download the password checker here and you'll need the encrypted flag in the same directory too.

## Hints
There are three hints:
> To view the file in the webshell, do: $ nano level1.py
> To exit nano, press Ctrl and x and follow the on-screen prompts.
> The str_xor function does not need to be reverse engineered for this challenge.

# Solving
## My Thoughts
I would classify this challenge as a mindset one.  It gets you used to how you need to think in order to solve a lot of CTF challenges, great for beginners!

## My First Script
Well we can try to open the flag, but get a bunch of garbage that looks like this:

``` bash
└─$ cat level1.flag.txt.enc
[gE]__TgS^S

           J                                                                                                          
```

Encrypted indeed!  Let's take a look at the code for the password checking script, I've commented it out (except for the part that's not relevant for the 'spirit' of the challenge):

``` python
### THIS FUNCTION WILL NOT HELP YOU FIND THE FLAG --LT ########################
def str_xor(secret, key):
    #extend key to secret length
    new_key = key
    i = 0
    while len(new_key) < len(secret):
        new_key = new_key + key[i]
        i = (i + 1) % len(key)
    return "".join([chr(ord(secret_c) ^ ord(new_key_c)) for (secret_c,new_key_c) in zip(secret,new_key)])
###############################################################################
# Opens and reads in the flag, the rb below indicates that it's reading in the file as binary data.
flag_enc = open('level1.flag.txt.enc', 'rb').read()

# Sets up a function
def level_1_pw_check():
    # Takes in user input as the password
    user_pw = input("Please enter correct password for flag: ")
    # Compares the user's input to the string "8713", if it's a match it prints out the flag.
    if( user_pw == "8713"):
        print("Welcome back... your flag, user:")
        # It runs the binary data through the encryption algorithm at the top of the script to decrypt it.
        decryption = str_xor(flag_enc.decode(), user_pw)
        print(decryption)
        return
    # Otherwise it informs you that the password was wrong.
    print("That password is incorrect")

# Will call the level_1_pw_check() function as soon as the script is ran.
level_1_pw_check()
```

Well, looks like our password is '8713', let's give it a try:

``` bash
└─$ python level1.py
Please enter correct password for flag: 8713
Welcome back... your flag, user:
picoCTF{545h_r1ng1ng_1b2fd683}
```

Looks like we got the flag! Nice!
