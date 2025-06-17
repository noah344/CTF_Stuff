# DISKO 1
This was a challenge listed exclusively for the Pico Gym.  It's listed as Easy and categorized as a Forensics challenge.  
Direct Link:  https://play.picoctf.org/practice/challenge/505

## Description
The Description reads:
> Can you find the flag in this disk image?

## Hints
There is one hint:
> Maybe Strings could help? If only there was a way to do that?

# Solving
## My Thoughts
A fairly simple challenge that was very similar to some other challenges, not too happy with this one.

## Analyzing the Image
We can just use wget and the link provided to download the image to our machine:

``` bash
┌──(noah㉿kali)-[~/picoctf/gym/DISKO_1]
└─$ wget https://artifacts.picoctf.net/c/538/disko-1.dd.gz -q; ls
disko-1.dd.gz
```

Now we should unpack the dd so we can take a look:

``` bash
┌──(noah㉿kali)-[~/picoctf/gym/DISKO_1]
└─$ gunzip disko-1.dd.gz; ls
disko-1.dd
```

I usually run strings on any sort of binary file like this just to see what we can find, let's also grep for pico to see if we can just get the flag:

``` bash
┌──(noah㉿kali)-[~/picoctf/gym/DISKO_1]
└─$ strings disko-1.dd | grep pico
:/icons/appicon
# $Id: piconv,v 2.8 2016/08/04 03:15:58 dankogai Exp $
piconv -- iconv(1), reinvented in perl
  piconv [-f from_encoding] [-t to_encoding]
  piconv -l
  piconv -r encoding_alias
  piconv -h
B<piconv> is perl version of B<iconv>, a character encoding converter
a technology demonstrator for Perl 5.8.0, but you can use piconv in the
piconv converts the character encoding of either STDIN or files
Therefore, when both -f and -t are omitted, B<piconv> just acts
picoCTF{1t5_ju5t_4_5tr1n9_e3408eef}
```

And there it is!
