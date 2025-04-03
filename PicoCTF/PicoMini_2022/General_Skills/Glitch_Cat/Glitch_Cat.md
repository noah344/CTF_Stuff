# Glitch Cat
This was a challenge for PicoMini 2022.  It's listed as Easy and categorized as a General Skills challenge.  
Direct Link: https://play.picoctf.org/practice/challenge/242

## Description
The Description reads:
> Our flag printing service has started glitching!

## Hints
There are three hints:
> ASCII is one of the most common encodings used in programming
> We know that the glitch output is valid Python, somehow!
> Press Ctrl and c on your keyboard to close your connection and return to the command prompt.

# Solving
## My Thoughts
This challenge was very similar to one that I had already written up previously, so details will be a little sparse!

## Weird Flag
When we connect to the server we get some weird output:

``` bash
└─$ nc saturn.picoctf.net 63870
'picoCTF{gl17ch_m3_n07_' + chr(0x39) + chr(0x63) + chr(0x34) + chr(0x32) + chr(0x61) + chr(0x34) + chr(0x35) + chr(0x64) + '}'
```

From previous experience, we know that the above chr(0x39) is python code for getting the character that corresponds to the hex code 0x39.  Let's open a python interactive prompt and just toss that string in:

``` bash
└─$ python
Type "help", "copyright", "credits" or "license" for more information.
>>> 'picoCTF{gl17ch_m3_n07_' + chr(0x39) + chr(0x63) + chr(0x34) + chr(0x32) + \
chr(0x61) + chr(0x34) + chr(0x35) + chr(0x64) + '}'
'picoCTF{gl17ch_m3_n07_9c42a45d}'
```

Theres our flag!
