# Information
Information is a challenge by SUSIE from picoCTF 2021 now in the picoGym worth 10 points.\
It's under the "General Skills" category.\
Direct Link: https://play.picoctf.org/practice/challenge/186

## Description
Files can always be changed in a secret way.  Can you find the flag? cat.jpg\
(Note, I won't be uploading the cat.jpg file here, you'll have to donwload it from the challenge).

## Hints
Hint 1:  Look at the details of the file.\
Hint 2:  Make sure to submit the flag as picoCTF(xxxxx}.

## Solution
This challenge is actually quite tricky considering the number of points you get, and if you haven't seen something like this before you'll probably struggle quite a bit.\
Something very very common in CTF's is something called base64, it's quite complicated so go ahead and give this a read:  https://builtin.com/software-engineering-perspectives/base64-encoding\
Basically, if you see a random string of uppercase, lowercase, and number characters, there's a good chance that it's actually a base64 encoded string.

So, now that we've got that out of the way, let's get to the actual challenge.  We've been provided a picture of a cat, very cute! But there's apparently something hiding within.\
Let's start simple and try to look at some of the exif data.  Exif data is basically data about a picture, it can include anything from the location the picture was taken to...perhaps a flag for a CTF?

Kali has a cool built in tool called exiftool that allows you to extract and very easily view the exif data within, so lets try that:

![image](https://github.com/noah344/CTF_Stuff/assets/17501232/75cae211-97f1-44a1-bccb-73bb3d47fc23)

Hmm, no flag here.  But wait, there's an interesting looking field in there:

![image](https://github.com/noah344/CTF_Stuff/assets/17501232/6a2e3d8d-c22f-4a83-9818-08a21f9d3f52)

That sure looks like base64 encoded text to me! Let's check with another builtin kali tool called, surprise surprise, base64! Check it out below:

![image](https://github.com/noah344/CTF_Stuff/assets/17501232/6528183b-c854-47c7-8dda-3381ea5b1f24)

And there it is! Like I said, this one would be reeeeeally hard for a newbie especially with how unhelpful the hints are.
