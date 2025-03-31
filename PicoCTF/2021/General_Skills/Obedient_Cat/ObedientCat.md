# Obedient Cat
This was a challenge listed in PicoCTF 2021.  It's listed as easy and categorized as a General Skills challenge.\
Direct Link:  https://play.picoctf.org/practice/challenge/147

## Description
The Description reads:
> This file has a flag in plain sight (aka "in-the-clear").

## Hints
There are three hints for this challenge:
> Any hints about entering a command into the Terminal (such as the next one), will start with a '$'... everything after the dollar sign will be typed (or copy and pasted) into your Terminal.\
> To get the file accessible in your shell, enter the following in the Terminal prompt: $ wget https://mercury.picoctf.net/static/217686fc11d733b80be62dcfcfca6c75/flag\
> $ man cat

# Solving
## My Thoughts
This was another great intro challenge for people just starting out in CTFs.

## Cat
This one is an easy one if you've ever messed with Linux.  You'll want to save the flag to a Linux OS and then simply run the command "cat flag" to view the flag.  Note that you could simply open the file with a text editor and view the flag, but I'm going to try to keep with the "spirit" of the challenge during these writeups.

You can follow the step by step below:
1. Download the "flag" file from the Obedient Cat challenge to your Linux VM.  On Kali, the default download folder for FireFox is /home/kali/Downloads/.  Check out the article on the wiki for navigating around Kali, I won't get into details on that here.
2. Open a console and navigate to the folder the flag is in, in my case I ran the command "cd /home/kali/Downloads/".
3. Now run the following command to view the contents of the file "cat flag".  You should now see the flag there and can input it into picoCTF!
![image](https://github.com/noah344/CTF_Stuff/assets/17501232/484f39b8-7a27-4e09-a2dc-5a76aa1764ac)

## Additional Resources
The cat command is extremely versatile, even Linux pros probably don't know everything.  The below link is a great resource for learning some of it's applications:
https://www.geeksforgeeks.org/cat-command-in-linux-with-examples/
