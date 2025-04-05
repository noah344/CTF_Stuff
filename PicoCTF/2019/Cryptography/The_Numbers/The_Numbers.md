# The Numbers
This was a challenge for PicoCTF 2019.  It's listed as Easy and categorized as a Cryptography challenge.  
Direct Link: https://play.picoctf.org/practice/challenge/68

## Description
The Description reads:
> The numbers... what do they mean?

## Hints
There is one hint:
> The flag is in the format PICOCTF{}

# Solving
## My Thoughts
Another annoying cipher challenge that has no real world relevance.

## Cipher
We are provided with the below image:

![Cipher](https://github.com/user-attachments/assets/af40e260-689d-4f5b-86ca-21885fa47282)

We can see that the symbols are not ciphered which means that none of the text was moved around.

We can also see that there are 7 characters before the { which corresponds directly with picoctf, so 1 set of numbers per character.  
We can see that there are no letters and numbers go higher than 9 which means its not in hex and probably not base64.  
p happens to be the 16th letter in the alphabet, so we're likely dealing with a cipher known as a1z26, where each letter is given a corresponding number for 1 to 26.

We could take the time to decode it ourselves, or we could plug it into cyberchef and have it do it instead:

![decoded](https://github.com/user-attachments/assets/ec0d9964-d5d5-41a5-a664-59447190fdf2)

So our flag is:  'picoCTF{thenumbersmason}'.
