# strings it
This was a challenge for PicoCTF 2019.  It's listed as Easy and categorized as a General Skills challenge.  
Direct Link: https://play.picoctf.org/practice/challenge/37

## Description
The Description reads:
> Can you find the flag in file without running it?

## Hints
There is one hint:
> strings

# Solving
## My Thoughts
Another simple challenge solvable with strings.

## Solving
I downloaded the file and, as per the instructions, I used strings.  There was a lot of output so I used grep to narrow down the results and got the flag:

``` bash
┌──(kali㉿kali)-[~/garden]
└─$ strings strings | grep pico
picoCTF{5tRIng5_1T_827aee91}
```
