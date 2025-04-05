# 2Warm
This was a challenge for PicoCTF 2019.  It's listed as Easy and categorized as a General Skills challenge.  
Direct Link: https://play.picoctf.org/practice/challenge/86

## Description
The Description reads:
> Can you convert the number 42 (base 10) to binary (base 2)? 

## Hints
There is one hint:
> Submit your answer in our competition's flag format. For example, if your answer was '11111', you would submit 'picoCTF{11111}' as the flag.

# Solving
## My Thoughts
This was a very simple challenge, not sure if it's really worth doing at all.

## Decimal to Hex
We could just plug this into the calculator and get it, but let's do the conversion by hand.

Generally, it's easier to first conver the number to hex and then to binary so let's do that.  Decimal is known as base 10, as shown below:

```
0 - 0 1 2 3 4 5 6 7 8 9
1 - 0 1 2 3 4 5 6 7 8 9
2 - 0 1 2 3 4 5 6 7 8 9
...
```

Hexadecimal is base 16 as shown below:

```
0 - 0 1 2 3 4 5 6 7 8 9 A B C D E F
1 - 0 1 2 3 4 5 6 7 8 9 A B C D E F
...
9 - 0 1 2 3 4 5 6 7 8 9 A B C D E F
A - 0 1 2 3 4 5 6 7 8 9 A B C D E F
```

So how do we convert them?  With remainders! % is a sign called modulus, instead of doing a full division, it tries to divide by the number provided until it can't anymore, then it'll just give you the remainder:

```
42 % 16 = 2 remainder 10.
So the last hex character will be 10, or A.
2 is not divisible by 16 further, so the other character will be 2.
42 in hex is 2A!
```

## Hex to Binary
Now converting hex to binary is very simple.  We simply separate the hex characters, each character will be 4 binary characters, we can do the same remainder method as well!

```
First Block
-----------
10 % 2 = 5 remainder 0
5 % 2 = 2 remainder 1
2 % 2 = 1 remainder 0
1 % 2 = 0 remainder 1
First block = 1010

Second Block
2 % 2 = 1 remainder 0
1 % 2 = 0 remainder 1
Second block = 0010
```

So the binary for 42 is 0010 1010, we can leave off the 00 at the start and then toss it into our flag format and our final flag is "picoCTF{101010}".  Nice!
