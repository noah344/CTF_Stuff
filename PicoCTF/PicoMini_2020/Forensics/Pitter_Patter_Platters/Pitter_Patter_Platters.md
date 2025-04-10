# Pitter, Patter, Platters
This was a challenge for PicoMini 2020.  It's listed as Medium and categorized as a Forensics challenge.  
Direct Link: https://play.picoctf.org/practice/challenge/87

## Description
The Description reads:
> 'Suspicious' is written all over this disk image. Download suspicious.dd.sda1

## Hints
There are two hints:
> It may help to analyze this image in multiple ways: as a blob, and as an actual mounted disk.
> Have you heard of slack space? There is a certain set of tools that now come with Ubuntu that I'd recommend for examining that disk space phenomenon...

# Solving
## My Thoughts

## Strings It
As always, the very first thing I like to do with challenges that involve downloadable things is to run strings on it:

``` bash
┌──(kali㉿kali)-[~/picoctf/2020_mini/pitter_patter_platters]
└─$ strings suspicious.dd.sda1 | more
BOt_BOt_
UA;@
/mnt/sda1
dVAT
lost+found
boot
suspicious-file.txt
3di'|
tW:,]
Ht(*
2k7k7k7k7k7k7
...
```

There's a ton of data that we'll have to parse through, but in the first few lines we already see a weird file named 'suspiciou-file.txt'.

I output the strings data to a text file and then imported it with python and had it spit out only lines that were longer than 10 characters:

``` python
with open("./strings.txt") as file:
    lines = file.read().splitlines()

for i in lines:
    if len(i) > 10:
        print(i)
```

Which gave us some slightly more useful output, one line in particular stood out to me:

```
Nothing to see here! But you may want to look here -->
```

Ok, not a lot to go off of.

## Mounting
Let's go ahead and mount it and poke around:

``` bash
┌──(noah㉿kali)-[~/picoctf/2020_mini/pitter_patter_platters]
└─$ sudo mount suspicious.dd.sda1 /media/stuff
```

Sure enough that one suspicious-file.txt contained the text we saw earlier.  Nothing else was too interesting in there.  One of the hints mentioned slack space.

## Slack Space
Well what is slack space?  You can read about details [here](https://www.techtarget.com/whatis/definition/slack-space-file-slack-space), but it's essentially the unused storage space available when a file is created.  It will often contain residual data.

Interesting, but how do we see it?  Well with a hex viewer!  We get a hint in the form of the file, let's run xxd (a hex editor) and grep for that line to see what we can see!

``` bash
lqq(noah__kali)-[~/picoctf/2020_mini/pitter_patter_platters]
mq$ xxd suspicious.dd.sda1 | grep Nothing -A 10
00200400: 4e6f 7468 696e 6720 746f 2073 6565 2068  Nothing to see h
00200410: 6572 6521 2042 7574 2079 6f75 206d 6179  ere! But you may
00200420: 2077 616e 7420 746f 206c 6f6f 6b20 6865   want to look he
00200430: 7265 202d 2d3e 0a7d 0036 0062 0037 0064  re -->.}.6.b.7.d
00200440: 0035 0034 0039 0062 005f 0033 003c 005f  .5.4.9.b._.3.<._
00200450: 007c 004c 006d 005f 0031 0031 0031 0074  .|.L.m._.1.1.1.t
00200460: 0035 005f 0033 0062 007b 0046 0054 0043  .5._.3.b.{.F.T.C
00200470: 006f 0063 0069 0070 0000 0000 0000 0000  .o.c.i.p........
00200480: 0000 0000 0000 0000 0000 0000 0000 0000  ................
00200490: 0000 0000 0000 0000 0000 0000 0000 0000  ................
002004a0: 0000 0000 0000 0000 0000 0000 0000 0000  ................
```

There's something there!  Removing all of the extra fluff we get:  }6b7d549b_3<_|Lm_111t5_3b{FTCocip

Doing some reversing magic we get our flag:  picoCTF{b3_5t111_mL|_<3_b945d7b6}  Nice!
