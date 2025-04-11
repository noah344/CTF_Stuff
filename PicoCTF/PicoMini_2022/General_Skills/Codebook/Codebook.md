# Codebook
This was a challenge for PicoMini 2022.  It's listed as Easy and categorized as a General Skills challenge.  
Direct Link: https://play.picoctf.org/practice/challenge/238

## Description
The Description reads:
> Run the Python script code.py in the same directory as codebook.txt.

## Hints
There are two hints:
> On the webshell, use ls to see if both files are in the directory you are in
> The str_xor function does not need to be reverse engineered for this challenge.

# Solving
## My Thoughts
This was almost too simple even for a beginner challenge.

## Easy Peazy
Simply use wget to download the files:

``` bash
┌──(kali㉿kali)-[~/codebook]
└─$ wget https://artifacts.picoctf.net/c/1/code.py
--2025-04-05 14:20:03--  https://artifacts.picoctf.net/c/1/code.py
Resolving artifacts.picoctf.net (artifacts.picoctf.net)... 3.167.88.6, 3.167.88.69, 3.167.
Connecting to artifacts.picoctf.net (artifacts.picoctf.net)|3.167.88.6|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 1278 (1.2K) [application/octet-stream]
Saving to: 'code.py'

code.py                                  100%[============================================

2025-04-05 14:20:04 (18.0 MB/s) - 'code.py' saved [1278/1278]


┌──(kali㉿kali)-[~/codebook]
└─$ wget https://artifacts.picoctf.net/c/1/codebook.txt
--2025-04-05 14:20:11--  https://artifacts.picoctf.net/c/1/codebook.txt
Resolving artifacts.picoctf.net (artifacts.picoctf.net)... 3.167.88.36, 3.167.88.74, 3.167
Connecting to artifacts.picoctf.net (artifacts.picoctf.net)|3.167.88.36|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 27 [application/octet-stream]
Saving to: 'codebook.txt'

codebook.txt                             100%[============================================

2025-04-05 14:20:11 (18.7 MB/s) - 'codebook.txt' saved [27/27]
```

We then need to make the code.py file executable:

``` bash
┌──(kali㉿kali)-[~/codebook]
└─$ chmod +x code.py; ls -l
total 8
-rwxrwxr-x 1 kali kali 1278 Mar 15  2023 code.py
-rw-rw-r-- 1 kali kali   27 Mar 15  2023 codebook.txt
```

Then we can run the script:

``` bash
┌──(kali㉿kali)-[~/codebook]
└─$ python code.py
picoCTF{c0d3b00k_455157_d9aa2df2}
```

And there we have the flag!
