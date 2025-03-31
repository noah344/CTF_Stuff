# runme.py
This was a challenge for PicoMini 2022.  It's listed as Easy and categorized as a General Skills challenge.  
Direct Link: https://play.picoctf.org/practice/challenge/250

## Description
The Description reads:
> Run the runme.py script to get the flag.
> Download the script with your browser or with wget in the webshell.

## Hints
There are four hints that read:
> If you have Python on your computer, you can download the script normally and run it. Otherwise, use the wget command in the webshell.

> To use wget in the webshell, first right click on the download link and select 'Copy Link' or 'Copy Link Address'

> Type everything after the dollar sign in the webshell: $ wget , then paste the link after the space after wget and press enter. This will download the script for you in the webshell so you can run it!

> Finally, to run the script, type everything after the dollar sign and then press enter: $ python3 runme.py You should have the flag now!

# Solving
## My Thoughts
Well the hints pretty much cover it!  This is supposed to be a very basic intro challenge and it's great at doing just that.

## Quick and Easy
It's as simple as running the script!

``` bash
┌──(noah㉿kali)-[~/runme.py]
└─$ wget https://artifacts.picoctf.net/c/34/runme.py
--2025-03-31 14:06:09--  https://artifacts.picoctf.net/c/34/runme.py
HTTP request sent, awaiting response... 200 OK
Length: 270 [application/octet-stream]
Saving to: 'runme.py'

runme.py            100%[===================>]     270  --.-KB/s    in 0s

2025-03-31 14:06:10 (176 MB/s) - 'runme.py' saved [270/270]

┌──(kali㉿kali)-[~/runme.py]
└─$ ls
runme.py

┌──(kali㉿kali)-[~/runme.py]
└─$ chmod +x runme.py

┌──(kali㉿kali)-[~/runme.py]
└─$ ./runme.py
picoCTF{run_s4n1ty_run}
```

Flag gotten!
