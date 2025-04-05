# First Grep
This was a challenge for PicoCTF 2019.  It's listed as Easy and categorized as a General Skills challenge.  
Direct Link: https://play.picoctf.org/practice/challenge/85

## Description
The Description reads:
> Can you find the flag in file? This would be really tedious to look through manually, something tells me there is a better way.

## Hints
There is one hint:
> grep tutorial

# Solving
## My Thoughts
Great little tutorial for grep.  Would like for it to have included command chaining somehow.

## Grep
Let's first take a look at the file we downloaded:

``` bash
┌──(kali㉿kali)-[~/first_grep]
└─$ cat file
Js!x/j5`4i6WsQOY-_/8@2~@Xne7S/gwg 8]>.Yf%iLx.*,GMAc(S:d` +Bi*fb)-kX8tauzGF6<~ywF]&-BQT-b-+2( J.#/JhE...
```

Wow, lots of junk in there.  Luckily we can use a builtin Linux tool called grep to search through the file for specific text we are looking for.  Grep will parse through files and only output lines that match the user's input.

Let's run grep for the text 'picoCTF' and see what we get:

``` bash
┌──(kali㉿kali)-[~/first_grep]
└─$ grep picoCTF file
picoCTF{grep_is_good_to_find_things_f77e0797}
```

There's the flag!
