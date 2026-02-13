# Magikarp Ground Mission
This was a challenge for PicoCTF 2021.  It's listed as Easy and categorized as a General Skills challenge.  
Direct Link: https://play.picoctf.org/practice/challenge/189

## Description
The Description reads:
> Do you know how to move between directories and read files in the shell? Start the container, `ssh` to it, and then `ls` once connected to begin. Login via `ssh` as `ctf-player` with the password, `6dee9772`

## Hints
There is one hint:
> Finding a cheatsheet for bash would be really helpful!

# Solving
## My Thoughts
This is a nice intro challenge to learn about navigating around Linux.

## Navigating Linux
We first login using ssh and the instructions provided.  Lets do ls and see what we have in our home directory:

``` bash
ctf-player@pico-chall$ ls
1of3.flag.txt  instructions-to-2of3.txt
```

Looks like a couple text files, lets cat them and see what they say:

``` bash
ctf-player@pico-chall$ cat *
picoCTF{xxsh_
Next, go to the root of all things, more succinctly `/`
```

Ok so we have the first of three parts of the flag 'picoCTF{xxsh_' and a hint that the next part is in the root, so lets navigate there, run ls, and then cat the files there:

``` bash
ctf-player@pico-chall$ ls /; cat /2of3.flag.txt; cat /instructions-to-3of3.txt
2of3.flag.txt  dev   instructions-to-3of3.txt  media  proc  sbin  tmp
bin            etc   lib                       mnt    root  srv   usr
boot           home  lib64                     opt    run   sys   var
0ut_0f_\/\/4t3r_
Lastly, ctf-player, go home... more succinctly `~`
```

So the second flag is '0ut_0f_\/\/4t3r_' and our next flag is apparently in the user's home directory, let's go there and cat the last file:

``` bash
ctf-player@pico-chall$ cd ~; ls; cat 3of3.flag.txt
3of3.flag.txt  drop-in
540e4e79}
```

So our full flag is 'picoCTF{xxsh_0ut_0f_\/\/4t3r_540e4e79}', nice!

