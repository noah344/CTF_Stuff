# Big Zip
This was a challenge listed exclusively for the Pico Gym.  It's listed as Easy and categorized as a General Skills challenge.  
Direct Link:  https://play.picoctf.org/practice/challenge/322

## Description
The Description reads:
> Unzip this archive and find the flag.

## Hints
There is a single hint that reads:
> Can grep be instructed to look at every file in a directory and its subdirectories?

# Solving
## My Thoughts
Simple challenge that teaches some concepts about linux CLI navigation.

## Grepping
We are provided with a single zipped folder named big-zip-files.zip.  We can unzip it using the below command:

``` bash
└─$ unzip big-zip-files.zip | less
Archive:  big-zip-files.zip
   creating: big-zip-files/
 extracting: big-zip-files/jpvaawkrpno.txt
  inflating: big-zip-files/oxbcyjsy.txt
  inflating: big-zip-files/hllhxlvvdgiii.txt
  inflating: big-zip-files/bdvnqbuutefealgveyiqd.txt
  inflating: big-zip-files/fudfsewmaafsbniiyktzr.txt
   creating: big-zip-files/folder_fqmjtuthge/
...
```

There's a lot more output there than what I show, but you get the general idea.\
There are many many folders and files within those folders insize of the zip.\
Our goal is to find the flag within one of those files.  But how?

We can use grep like below to search through files in the local directory:

``` bash
┌──(kali㉿kali)-[~/gym/big_zip/big-zip-files]
└─$ grep 'pico' *
grep: folder_cqwqkwgnco: Is a directory
grep: folder_edjlqfyqrh: Is a directory
grep: folder_fqmjtuthge: Is a directory
grep: folder_knqqchrayk: Is a directory
grep: folder_qhscwikodv: Is a directory
grep: folder_rzmrqygplj: Is a directory
grep: folder_uxvqunebny: Is a directory
grep: folder_zcnvekqcsp: Is a directory
```

But like I said, this only covers the local directory, it doesn't recursively look inside of the folders.  A little on grep in case you aren't familiar,\
grep will search for user provided text within specified files.  So the command "grep 'pico' *" is searching for the word 'pico' within any file in the local directory.

We can add the -r flag to the command to have it search through everything recursively!

``` bash
└─$ grep -r 'pico' .
./folder_pmbymkjcya/folder_cawigcwvgv/folder_ltdayfmktr/folder_fnpfclfyee/whzxrpivpqld.txt:information on the record will last a billion years. Genes and brains and books encode picoCTF{gr3p_15_m4g1c_ef8790dc}
```

And there we go, if we want we can cat that file and see for ourselves:
``` bash
└─$ cat ./folder_pmbymkjcya/folder_cawigcwvgv/folder_ltdayfmktr/folder_fnpfclfyee/whzxrpivpqld.txt
information on the record will last a billion years. Genes and brains and books encode picoCTF{gr3p_15_m4g1c_ef8790dc}
```
