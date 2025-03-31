# Wave a Flag
Wave a flag is a challenge by SYREAL from picoCTF 2021 now in the picoGym worth 10 points.\
It's under the "General Skills" category.\
Direct Link:  https://play.picoctf.org/practice/challenge/170

## Description
Can you invoke help flags for a tool or binary? This program has extraordinarily helpful information...\
(Note, you should download the program from the challenge, I won't post it in Github).

## Hints
Hint 1:  This program will only work in the webshell or another Linux computer.\
Hint 2:  To get the file accessible in your shell, enter the following in the Terminal prompt: $ wget https://mercury.picoctf.net/static/beec4f433e5ee5bfcd71bba8d5863faf/warm\
Hint 3:  Run this program by entering the following in the Terminal prompt: $ ./warm, but you'll first have to make it executable with $ chmod +x warm\
Hint 4:  -h and --help are the most common arguments to give to programs to get more information from them!\
Hint 5:  Not every program implements help features like -h and --help.

## Solution
This is another pretty easy one, so I'll take the time to teach or explain a few things that might be useful in the future.\
First off, when you download the file, you might notice there's no extension to it as shown below:

![image](https://github.com/noah344/CTF_Stuff/assets/17501232/7d469546-f9cc-4f7a-acdd-a8f598b39bd9)

Unlike Windows, Linux doesn't require extensions.  While certainly helpful, Linux will use the contents of the file to determine what program it needs to be ran with.

One way of determining what type of file it is, is to use the "file" command, as shown below:

![image](https://github.com/noah344/CTF_Stuff/assets/17501232/34f5c7bd-3a97-4dcb-a23b-9eb652f62573)

This simply means that the file is a 64-bit executable, similar to an exe on windows.  Lets try to run it!

![image](https://github.com/noah344/CTF_Stuff/assets/17501232/a0d9bd96-2da5-4a91-9c1a-04900e174d9b)

Whoops! Looks like we need to update the permissions, perfect time to flex your googling skills and figure out how to enable execution of the file.

Ok, now we can run it and we get the below:

![image](https://github.com/noah344/CTF_Stuff/assets/17501232/6b07422c-89a8-4ade-98bf-4464d1af539e)

Sounds about right, lets add a -h flag to our command and see what we get:

![image](https://github.com/noah344/CTF_Stuff/assets/17501232/e1a2ce16-4695-4e61-9777-9cfee5b8c139)

And look at that, there's the flag! Fun fact, just about all Linux applications will have a help menu you can view with either -h or --help.  You can also try using man, which will open a manual for the tool if it's available.
