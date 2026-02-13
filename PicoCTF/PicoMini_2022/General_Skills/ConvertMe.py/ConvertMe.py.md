# ConvertMe.py
This was a challenge for PicoMini 2022.  It's listed as Easy and categorized as a General Skills challenge.  
Direct Link: https://play.picoctf.org/practice/challenge/239

## Description
The Description reads:
> Run the Python script and convert the given number from decimal to binary to get the flag.

## Hints
There are six hints:
> Look up a decimal to binary number conversion app on the web or use your computer's calculator!  
> The str_xor function does not need to be reverse engineered for this challenge.  
> If you have Python on your computer, you can download the script normally and run it. Otherwise, use the wget command in the webshell.
> To use wget in the webshell, first right click on the download link and select 'Copy Link' or 'Copy Link Address'
> Type everything after the dollar sign in the webshell: $ wget , then paste the link after the space after wget and press enter. This will download the script for you in the webshell so you can run it!
> Finally, to run the script, type everything after the dollar sign and then press enter: $ python3 convertme.py  

# Solving
## My Thoughts
Very simple challenge that has to do with converting decimal numbers to binary.

## Decimal to Binary
When we run the provided python script we are provided with the below output:

``` bash
└─$ python convertme.py
If 87 is in decimal base, what is it in binary base?
Answer:
```

We can open up a calculator and get the binary from the decimal like so:

![Decimal to Binary](https://github.com/user-attachments/assets/f0454579-b554-48ed-ba90-bfa726c10525)

So our answer should be '01010111', let's try it:

``` bash
└─$ python convertme.py
If 87 is in decimal base, what is it in binary base?
Answer: 01010111
That is correct! Here's your flag: picoCTF{4ll_y0ur_b4535_762f748e}
```

And there's our flag!
