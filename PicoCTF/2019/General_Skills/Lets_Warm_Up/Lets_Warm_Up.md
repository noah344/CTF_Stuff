# Lets Warm Up
This was a challenge for PicoCTF 2019.  It's listed as Easy and categorized as a General Skills challenge.  
Direct Link: https://play.picoctf.org/practice/challenge/22

## Description
The Description reads:
> If I told you a word started with 0x70 in hexadecimal, what would it start with in ASCII? 

## Hints
There is one hint:
> Submit your answer in our flag format. For example, if your answer was 'hello', you would submit 'picoCTF{hello}' as the flag.

# Solving
## My Thoughts
Intro challenge to hex/ascii.

## Solving
We could simply look up the hex code to see what character it corresponds with, but I figured it would be a good challenge to demonstrate a simple python command with.

You can use chr() with the hex within to convert a single hex encoded character to ascii as shown below:

``` python
>>> chr(0x70)
'p'
```
So our flag will be 'picoCTF{p}'.
