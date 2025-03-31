# Nice Netcat
This was a challenge listed in PicoCTF 2021.  It's listed as easy and categorized as a General Skills challenge.\
Direct Link:  https://play.picoctf.org/practice/challenge/156

## Description
The Description reads:
> There is a nice program that you can talk to by using this command in a shell:\
> $ nc mercury.picoctf.net 49039, but it doesn't speak English...

## Hints
There were two hints for this challenge:
> You can practice using netcat with this picoGym problem: what's a netcat?\
> You can practice reading and writing ASCII with this picoGym problem: Let's Warm Up

# Solving
## My Thoughts

## Netcat
Well, you might be wondering what that nc is up there in the command.  That's how you run netcat on Linux!  Well great but what's netcat?\
Simply put, netcat is a really simple way to connect to a network port and get some data.

So lets go ahead and run that command and see what happens:

![image](https://github.com/noah344/CTF_Stuff/assets/17501232/47eeae96-4a64-449b-a0c3-3e8853e4c2bd)

Well...that's something.  And it's another teachable moment!  ASCII, look it up!\
Basically, each character you type on your computer has a number code associated with it, here's a nice table for it:  https://www.asciitable.com/\
That output above sure does look like a list of ascii characters!

Now we could go through each line, one at a time but that'll take a bit and it's good scripting practice!  See the script in this folder, I've commented it out for easy reading.

And here I am running the script! Worked like a charm!

![image](https://github.com/noah344/CTF_Stuff/assets/17501232/e962edd2-7d77-4d22-9a97-125608081b66)
