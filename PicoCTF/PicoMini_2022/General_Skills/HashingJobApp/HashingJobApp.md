# HashingJobApp
This was a challenge for PicoMini 2022.  It's listed as Easy and categorized as a General Skills challenge.  
Direct Link: https://play.picoctf.org/practice/challenge/243

## Description
The Description reads:
> If you want to hash with the best, beat this test!

## Hints
There are two hints:
> You can use a commandline tool or web app to hash text
> Press Ctrl and c on your keyboard to close your connection and return to the command prompt.

# Solving
## My Thoughts
Without some additional insight, this challenge could probably be challenging for newer people primarily because of hidden characters.

## MD5
MD5 is a hashing algorithm, a type of one-way encryption.  Once it's encrypted, it is impossible to decrypt it.  The hash can be cracked by brute force, but not reversed.  The goal of this challenge is to calculate the md5 hash of various strings and provide them to the server.  After 3 correct answers, you are provided the flag.

On Linux, you can use the 'md5sum' command to calculate the md5 hash of text similar to the below:

``` bash
└─$ echo 'hashing is fun' | md5sum
e22f44baedc94c30d683e8cdffd0b6f7  -
```

The issue here is that md5sum is also interpretint hidden characters and echo outputs a \n (newline) character at the end of every string it outputs.  We can stop it from doing that using the -n flag shown below:

``` bash
└─$ echo -n 'hashing is fun' | md5sum
855b004cfb430625cab791206079fc33  -
```

Ok, let's try it out now:

``` bash
└─$ nc saturn.picoctf.net 64311
Please md5 hash the text between quotes, excluding the quotes: 'Corvettes'
Answer:
0d18e8c9500eebd5748b6ad225652080
0d18e8c9500eebd5748b6ad225652080
Correct.
Please md5 hash the text between quotes, excluding the quotes: 'having an operation'
Answer:
e8911c168f3f28c385ac7f3e4d0682cc
e8911c168f3f28c385ac7f3e4d0682cc
Correct.
Please md5 hash the text between quotes, excluding the quotes: 'computer hackers'
Answer:
1034abc8025edcc22f58c35abc21e36f
1034abc8025edcc22f58c35abc21e36f
Correct.
picoCTF{4ppl1c4710n_r3c31v3d_bf2ceb02}
```

There's the flag!
