# Warmed Up
This was a challenge for PicoCTF 2019.  It's listed as Easy and categorized as a General Skills challenge.  
Direct Link: https://play.picoctf.org/practice/challenge/58

## Description
The Description reads:
> What is 0x3D (base 16) in decimal (base 10)?

## Hints
There is one hint:
> Submit your answer in our flag format. For example, if your answer was '22', you would submit 'picoCTF{22}' as the flag.

# Solving
## My Thoughts
A simple challenge about converting hex to decimal.

## Hex to Decimal
Let's just go ahead and convert the hex:

```
3 D
D = 13 x 16^0 = 13 x 1 = 13
3 = 3 x 16^1 = 3 * 16 = 48
14 + 48 = 61
```

So our flag will be picoCTF{61}!
