# PW Crack 2
This was a challenge for PicoMini 2022.  It's listed as Easy and categorized as a General Skills challenge.  
Direct Link: https://play.picoctf.org/practice/challenge/246

## Description
The Description reads:
> Can you crack the password to get the flag?
> Download the password checker here and you'll need the encrypted flag in the same directory too.

## Hints
There are two hints:
> Does that encoding look familiar?
> The str_xor function does not need to be reverse engineered for this challenge.

# Solving
## My Thoughts
Another great intro challenge that introduces some basic encoding (base64).

## Base64
Let's take a look at the script again, I've commented out the relevant parts again:

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
# Opens the encrypted flag and reads it in as binary.
flag_enc = open('level2.flag.txt.enc', 'rb').read()

# Initializes a function.
def level_2_pw_check():
    # Gets the user inputted password.
    user_pw = input("Please enter correct password for flag: ")
    # Compares the password to the encoded password, if it's correct it decrypts the flag and prints it out.
    if( user_pw == chr(0x33) + chr(0x39) + chr(0x63) + chr(0x65) ):
        print("Welcome back... your flag, user:")
        decryption = str_xor(flag_enc.decode(), user_pw)
        print(decryption)
        return
    print("That password is incorrect")

level_2_pw_check()
```

Alright, so the key here is the below line:

``` python
chr(0x33) + chr(0x39) + chr(0x63) + chr(0x65)
```

Let's open up python really quick and check what the chr() function does:

``` python
Help on built-in function chr in module builtins:

chr(i, /)
    Return a Unicode string of one character with ordinal i; 0 <= i <= 0x10ffff.
 Help on chr line 1/4 (END) (press h for help or q to quit)
```

Not super helpful, without prior knowledge it's pretty hard to figure this out!  The text in that line is hexadecimal!  Generally any string that begins with a 0x will be hex.  
You can also verify encoded text is hex by checking if the string contains only 0-9 and a-f as those are the only characters that appear in hex.

Let's plug those hex codes into cyberchef and see what our password is:

![Hex Decoded](https://github.com/user-attachments/assets/6ca01976-b476-4943-9a44-084e9879c69f)

Cool now let's plug that into our script:

``` bash
└─$ python level2.py
Please enter correct password for flag: 39ce
Welcome back... your flag, user:
picoCTF{tr45h_51ng1ng_502ec42e}
```

Flag acquired!
