# Information
This was a challenge listed in PicoCTF 2021.  It's listed as easy and categorized as a Forensics challenge.

## Description
The Description reads:
> Files can always be changed in a secret way.\
> Can you find the flag?

## Hints
There are two hints that reads:
> Look at the details of the file\
> Make sure to submit the flag as picoCTF{XXXXX}

# Solving
## My Thoughts
Had the hints been better, I would consider this to be a great intro challenge.  If somebody is unfamiliar with base64 encoding though, this challenge would be pretty much impossible.  I think this would have been much better if the flag was stored in cleartext inside of the exif data.

## cat.jpg
This challenge is actually quite tricky considering the number of points you get, and if you haven't seen something like this before you'll probably struggle quite a bit.\
Something very very common in CTF's is something called base64, it's quite complicated so go ahead and give this a read:  https://builtin.com/software-engineering-perspectives/base64-encoding\
Basically, if you see a random string of uppercase, lowercase, and number characters, there's a good chance that it's actually a base64 encoded string.  Depending on how long the string is, you may also see it end in an = or ==.

So, now that we've got that out of the way, let's get to the actual challenge.  We've been provided a picture of a cat, very cute! But there's apparently something hiding within.\
Let's start simple and try to look at some of the exif data.  Exif data is basically data about a picture, it can include anything from the location the picture was taken to...perhaps a flag for a CTF?

Kali has a cool built in tool called exiftool that allows you to extract and very easily view the exif data within, so lets try that:

![image](https://github.com/noah344/CTF_Stuff/assets/17501232/75cae211-97f1-44a1-bccb-73bb3d47fc23)

Hmm, no flag here.  But wait, there's an interesting looking field in there:

![image](https://github.com/noah344/CTF_Stuff/assets/17501232/6a2e3d8d-c22f-4a83-9818-08a21f9d3f52)

That sure looks like base64 encoded text to me! Let's check with another builtin kali tool called, surprise surprise, base64! Check it out below:

![image](https://github.com/noah344/CTF_Stuff/assets/17501232/6528183b-c854-47c7-8dda-3381ea5b1f24)

And there it is! Like I said, this one would be really difficult for somebody not familiar with the concept, especially with how unhelpful the hints are.
