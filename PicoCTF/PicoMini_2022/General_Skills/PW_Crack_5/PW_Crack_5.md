# PW Crack 5
This was a challenge for PicoMini 2022.  It's listed as Medium and categorized as a General Skills challenge.  
Direct Link: https://play.picoctf.org/practice/challenge/249

## Description
The Description reads:
> Can you crack the password to get the flag?
> Download the password checker here and you'll need the encrypted flag and the hash in the same directory too.
> Here's a dictionary with all possible passwords based on the password conventions we've seen so far.

## Hints
There are three hints:
> Opening a file in Python is crucial to using the provided dictionary.
> You may need to trim the whitespace from the dictionary word before hashing. Look up the Python string function, strip
> The str_xor function does not need to be reverse engineered for this challenge.

# Solving
## My Thoughts
Simple python basics challenge.

## Solving
For this challenge we just need to read in the dictionary file and try to crack the password with that, below is the updated code that I used:

``` python
import hashlib

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

flag_enc = open('level5.flag.txt.enc', 'rb').read()
correct_pw_hash = open('level5.hash.bin', 'rb').read()

def hash_pw(pw_str):
    pw_bytes = bytearray()
    pw_bytes.extend(pw_str.encode())
    m = hashlib.md5()
    m.update(pw_bytes)
    return m.digest()


def level_5_pw_check():
    with open("./dictionary.txt") as file:
        lines = file.read().splitlines()

    for user_pw in lines:
        if( hash_pw(user_pw.strip()) == correct_pw_hash ):
            print("Welcome back... your flag, user:")
            decryption = str_xor(flag_enc.decode(), user_pw)
            print(decryption)
            return

level_5_pw_check()
```

And when we run it:

``` bash
┌──(kali㉿kali)-[~/picoctf/2022_mini/pw_crack_5]
└─$ python level5.py
Welcome back... your flag, user:
picoCTF{h45h_sl1ng1ng_40f26f81}
```
