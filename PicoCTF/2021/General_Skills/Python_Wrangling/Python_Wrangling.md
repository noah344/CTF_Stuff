# Python Wrangling
This was a challenge listed in PicoCTF 2021.  It's listed as easy and categorized as a General Skills challenge.\
Direct Link:  https://play.picoctf.org/practice/challenge/166

## Description
The Description reads:
> Python scripts are invoked kind of like programs in the Terminal...\
> Can you run this python script using this password to get the flag?

## Hints
There are two hints for this challenge:
> Get the Python script accessible in your shell by entering the following command in the Terminal prompt: $ wget https://mercury.picoctf.net/static/5c4c0cbfbc149f3b0fc55c26f36ee707/ende.py\
> $ man python

# Solving
## My Thoughts
Super easy intro challenge for Python.

## Python
This one's another simple one but I think there's some extra learning that can be done here.\
We are provided with a python file, why not go through and comment it out to see what it's doing? I uploaded my commented file for you to look through.

I'd encourage you do the same on your own and then compare with what I got, google is your friend here!  This is one of the best ways to learn python.

Ok, now that we've got that done, lets solve the actual challenge.  All we need to do is run the python script with the supplied password to decrypt the supplied flag file.
Follow the below steps:

Start by downloading the password file, ende.py file, and flag.txt file and place them in the same folder somewhere on your OS.\
We've got the files but what do we do with them? Well, typically python scripts (and most other scripts for that matter) need to be ran from the command line.\
So lets go ahead and open a console in that folder and see what we can do.  Run the "ls" command and verify that the folder contents look similar to the below screenshot:

![image](https://github.com/noah344/CTF_Stuff/assets/17501232/b28449ff-ffc5-479c-a03d-0293267e5e48)

Let's see what's in that pw.txt file, just run "cat pw.txt" and you should get output similar to the below screenshot:

![image](https://github.com/noah344/CTF_Stuff/assets/17501232/69a3a416-6bf2-4c84-aa6e-a9abe9239b36)

Looks like just a random string of numbers, lets hold onto that so we can use it later.

Ok, lets try to run that python script now.  Python is USUALLY installed by default on Linux, even with the most bare-bones installations.  The most fullproof way of running one of these .py files is to just run "python ende.py".\
You should get output similar to the below screenshot:

![image](https://github.com/noah344/CTF_Stuff/assets/17501232/572f4e11-5e05-45d9-84e4-004f897e9ce8)

Ok, interesting.  A common thing to have in most programs/scripts is help documentation.  On linux this can usually be accessed by adding a -h to our command output, lets try that "python ende.py -h":

![image](https://github.com/noah344/CTF_Stuff/assets/17501232/5087ef10-e0a7-4f9f-a260-5625ca217a6c)

That's some awfully helpful help output, lets try it now! Run "python ende.py -d flag.txt.en", it'll prompt you for a password which we conveniently grabbed earlier!\
Output after entering the password should look like the below:

![image](https://github.com/noah344/CTF_Stuff/assets/17501232/e45ff1e7-fd47-405d-952f-4aca295262db)

And there it is! Flag gotten.
