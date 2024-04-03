# Mod 26
Mod 26 is a challenge by PANDU from picoCTF 2021 now in the picoGym worth 10 points.\
Direct Link:  https://play.picoctf.org/practice/challenge/144

## Description
Cryptography can be easy, do you know what ROT13 is?\
cvpbPGS{arkg_gvzr_V'yy_gel_2_ebhaqf_bs_ebg13_jdJBFOXJ}

## Hints
Hint 1:  This can be solved online if you don't want to do it by hand!

## Solution
With this challenge only being worth 10 points, it should be relatively easy.  With a lot of CTF challenges, there will be hints not only in the description, but also in the title.

So we have two things to look into based on the title and description, Mod 26 and ROT13.  A quick google search turns up a bunch of results for ROT13, I started with Wikipedia:  https://en.wikipedia.org/wiki/ROT13

ROT13 is a type of cryptographic cypher known as a simple substitution cypher that simply replaces a letter with the 13th letter after it in the alphabet.\
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

Now, I'm not going to lie, I didn't do this by hand, hopefully you didn't either! If you just google online for a ROT13 decoder, you can find plenty online.

I also thought it would be a nice little exercise to write a script for this, you can find it in the Mod 26 folder.  Definitely went way overboard on it as well and commented it out as much as I could to make it easy to understand!
