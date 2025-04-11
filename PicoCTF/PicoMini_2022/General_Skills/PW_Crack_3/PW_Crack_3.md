# PW Crack 3
This was a challenge for PicoMini 2022.  It's listed as Medium and categorized as a General Skills challenge.  
Direct Link: https://play.picoctf.org/practice/challenge/247

## Description
The Description reads:
> Can you crack the password to get the flag?
> Download the password checker here and you'll need the encrypted flag and the hash in the same directory too.
> There are 7 potential passwords with 1 being correct.
> You can find these by examining the password checker script.

## Hints
There are three hints:
> To view the level3.hash.bin file in the webshell, do: $ bvi level3.hash.bin
> To exit bvi type :q and press enter.
> The str_xor function does not need to be reverse engineered for this challenge.

# Solving
## My Thoughts
This was a dumb challenge.  At medium the user should have to decode the password themselves.

## Solving
The script has the 7 possible passwords listed at the bottom:

```
pos_pw_list = ["f09e", "4dcf", "87ab", "dba8", "752e", "3961", "f159"]
```

Just keep running the script using different passwords until you get the flag:

``` bash
┌──(kali㉿kali)-[~/picoctf/2022_mini/pw_crack_3]
└─$ python level3.py
Please enter correct password for flag: 87ab
Welcome back... your flag, user:
picoCTF{m45h_fl1ng1ng_cd6ed2eb}
```

Yay.
