# Tab, Tab, Attack
This was a challenge for PicoCTF 2021.  It's listed as Easy and categorized as a General Skills challenge.  
Direct Link: https://play.picoctf.org/practice/challenge/176

## Description
The Description reads:
> Using tabcomplete in the Terminal will add years to your life, esp. when dealing with long rambling directory structures and filenames: Addadshashanammu.zip

## Hints
There is one hint:
> After `unzip`ing, this problem can be solved with 11 button-presses...(mostly Tab)...

# Solving
## My Thoughts
This was a nice simple challenge that introduces tab completion to new Linux users.

## Tab Completion
Now we could do this the way it suggests, but I prefer my method.  After unzipping, let's run an 'find -type f', which will find all files within the current directory:

``` bash
┌──(kali㉿kali)-[~/tab_tab_attack]
└─$ find -type f
./Addadshashanammu/Almurbalarammi/Ashalmimilkala/Assurnabitashpi/Maelkashishi/Onnissiralis/Ularradallaku/fang-of-haynekhtnamet
```

So we have a file located at the above spot, let's navigate to that folder and run file to see what the file is:

``` bash
┌──(kali㉿kali)-[~/tab_tab_attack]
└─$ cd Addadshashanammu/Almurbalarammi/Ashalmimilkala/Assurnabitashpi/Maelkashishi/Onnissiralis/Ularradallaku/; file *
fang-of-haynekhtnamet: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 3.2.0, BuildID[sha1]=47e898db922f38cb54ab4a08fb4e3def5a1cb6a1, not stripped
```

So, this is an executable file, let's run it:

``` bash
┌──(kali㉿kali)-[~/…/Assurnabitashpi/Maelkashishi/Onnissiralis/Ularradallaku]
└─$ ./fang-of-haynekhtnamet
*ZAP!* picoCTF{l3v3l_up!_t4k3_4_r35t!_a00cae70}
```

And there's our flag!
