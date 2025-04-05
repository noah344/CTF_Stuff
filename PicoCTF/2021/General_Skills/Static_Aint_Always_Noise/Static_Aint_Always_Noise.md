# Glitch Cat
This was a challenge for PicoCTF 2021.  It's listed as Easy and categorized as a General Skills challenge.  
Direct Link: https://play.picoctf.org/practice/challenge/163

## Description
The Description reads:
> Can you look at the data in this binary: static? This BASH script might help!

## Hints
There are no hints.

# Solving
## My Thoughts
A great intro to some useful Linux commands, not really a fan of the tool provided since there are easier/better to use ones.

## Strings
We are provided with an executable file as shown below, let's make sure to give it exec privileges as well:

``` bash
┌──(kali㉿kali)-[~/static]
└─$ chmod +x static; file static
static: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 3.2.0, BuildID[sha1]=639391a8b15c579d69659462d3c935fa61693f17, not stripped
```

As expected, it's an executable.  Let's try running it:

``` bash
┌──(kali㉿kali)-[~/static]
└─$ ./static
Oh hai! Wait what? A flag? Yes, it's around here somewhere!
```

Not super helpful.  Now, the very first thing I always do with every single binary challenge is run the Linux 'strings' command against it.  Even with compiled programs, you'll usually be able to pick out some valid strings within the file, let's try it out:

``` bash
┌──(noah㉿kali)-[~/static]
└─$ strings static
/lib64/ld-linux-x86-64.so.2
libc.so.6
puts
__cxa_finalize
__libc_start_main
GLIBC_2.2.5
_ITM_deregisterTMCloneTable
__gmon_start__
_ITM_registerTMCloneTable
AWAVI
AUATL
[]A\A]A^A_
Oh hai! Wait what? A flag? Yes, it's around here somewhere!
;*3$"
picoCTF{d15a5m_t34s3r_98d35619}
GCC: (Ubuntu 7.5.0-3ubuntu1~18.04) 7.5.0
crtstuff.c
deregister_tm_clones
__do_global_dtors_aux
completed.7698
```

Sure enough, the flag is right there!
