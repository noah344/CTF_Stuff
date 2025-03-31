# First Find
This was a challenge listed exclusively for the Pico Gym.  It's listed as Easy and categorized as a General Skills challenge.  
Direct Link:  [https://play.picoctf.org/practice/challenge/322](https://play.picoctf.org/practice/challenge/320)

## Description
The Description reads:
> Unzip this archive and find the file named 'uber-secret.txt'

## Hints
There are no hints for this challenge.

# Solving
## My Thoughts
For people unfamiliar with the Linux CLI and the various tools at your disposal, this is a great challenge for learning a bit./
A hint would be helpful even though the title and description contain hints as well.

## Find
In linux, there is a command called 'find', you can use this command to search recursively through the filesystem to find files that match the search string.\
So after we unzip the zip folder, we can simply run the command below to find the file we are looking for:

``` bash
└─$ find -type f | grep uber
./files/adequate_books/more_books/.secret/deeper_secrets/deepest_secrets/uber-secret.txt
```

Now it's as simple as running cat on the file and we get our flag:

``` bash
└─$ cat ./files/adequate_books/more_books/.secret/deeper_secrets/deepest_secrets
picoCTF{f1nd_15_f457_ab443fd1}
```
