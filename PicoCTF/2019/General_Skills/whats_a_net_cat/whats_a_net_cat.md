# what's a net cat?
This was a challenge for PicoCTF 2019.  It's listed as Easy and categorized as a General Skills challenge.  
Direct Link: https://play.picoctf.org/practice/challenge/34

## Description
The Description reads:
> Using netcat (nc) is going to be pretty important. Can you connect to jupiter.challenges.picoctf.org at port 25103 to get the flag?

## Hints
There is one hint:
> nc tutorial

# Solving
## My Thoughts
A lot of pico challenges require netcat to connect to ports and get the flag, this is an intro to that concept.

## Solving
As requested we simply connect to the server via netcat and get the flag:

``` bash
┌──(noah㉿kali)-[~/garden]
└─$ nc jupiter.challenges.picoctf.org 25103
You're on your way to becoming the net cat master
picoCTF{nEtCat_Mast3ry_d0c64587}
```
