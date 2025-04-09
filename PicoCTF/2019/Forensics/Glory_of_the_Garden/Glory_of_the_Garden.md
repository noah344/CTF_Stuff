# Glory of the Garden
This was a challenge for PicoCTF 2019.  It's listed as Easy and categorized as a Forensics challenge.  
Direct Link: https://play.picoctf.org/practice/challenge/44

## Description
The Description reads:
> This garden contains more than it seems.

## Hints
There is one hint:
> What is a hex editor?

# Solving
## My Thoughts
Very simple forensics intro challenge.

## Strings
The very first thing I do when downloading executables and images is run the "strings" command.  This command will open the file as binary and attempt to convert it to Ascii if possible.

You can see the bottom of the strings output below:

``` bash
┌──(kali㉿kali)-[~/garden]
└─$ strings garden.jpg
......
,~J|
u)(])F
={~5
h--@3
cZi-
M(.I
]hWP&
jc#k
=7g&
mjx/
s\]|."Ue
\qZf
Here is a flag "picoCTF{more_than_m33ts_the_3y33dd2eEF5}"
```

So we got our flag already!
