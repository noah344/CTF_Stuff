# Hashcrack
This was the fifth challenge listed in PicoCTF 2025.  It's listed as easy and categorized as a Cryptography challenge.

## Description
The Description reads:
> A company stored a secret message on a server which got breached due to the admin using weakly hashed passwords. Can you gain access to the secret stored within the server?

## Hints
There are three hints that read:
> Understanding hashes is very crucial.

> Can you identify the hash algorithm? Look carefully at the length and structure of each hash identified.

and
> Tried using any hash cracking tools?

# Solving
## My Thoughts
This was a super simple intro to hash cracking!  For people unfamiliar with the process this was probably a great way to learn some new things, I think it took maybe 2 minutes for me to solve since I've done similar things before.

## What is a hash?
Hashes are a special form of one-way encryption typically used to encrypt passwords.  On Linux specifically, when you create a new user, the password you enter is hashed and stored (usually) in the /etc/shadow file.  As it is a one-way encryption algorithm, there is no way to decrypt it!  When you plugin your password to login, the password you enter is hashed in exactly the same way and compared to the hash in the shadow file.  If they match you are granted access, if they don't you aren't!  It's that simple.

Now, like I said, hashes cannot be decrypted but they can be cracked!  There are a variety of ways to do this, from brute forcing to dictionary attacks.  Things like password salts make password cracking more difficult but we'll get into that in a future challenge.  Let's get into solving it!

## Connecting to the Server
When we connect to the server, we are greeted with the below:

![Connecting](https://github.com/user-attachments/assets/d33df862-6262-42cf-b1c4-457e12bae6e0)

So we are presented with what we can assume is a hash, and asked to enter the password.  Let's see if we can identify what that hash is using a nifty tool that comes with Kali called hash-identifer:

![hash-identifier](https://github.com/user-attachments/assets/53024526-6103-4fef-8fa5-cbabcc9fed6f)

Looks like it's most likely an unsalted MD5 hash! Easy enough, if the password is simple enough we should be able to run a dictionary attack against it to grab the password!

## What is a Dictionary Attack?
As I mentioned before, when you login, the password you enter is hashed and compared to the one stored in the shadow file.  If we have the actual hash, we can run an offline attack against the password using this same principle, we just need a huge list of passwords!

This is where rockyou comes in, rockyou is an infamous password list that comes default with Kali containing over 14 million passwords (and that's not even the biggest one out there).  

## Hashtcat
Hashcat is a fantastic tool for password cracking.  It's extremely scalable, can use both CPUs and GPUs for cracking, and can be used to crack hundreds of different types of hashes.  So let's try it out with hashcat!

We can do a few different things with it before we get started, if we simply run hashcat with the hash, it'll do something similar to hash-identifier and give some recommendations for us:

![Identifying Hashes with Hashcat](https://github.com/user-attachments/assets/9be8d82e-6c32-4d09-870e-fe3eca63bd25)

It's also recommending MD5 so let's try that, below is the command we're going to use:

``` bash
hashcat -m 0 -a 0 '482c811da5d5b4bc6d497ffa98491e38' /usr/share/wordlists/rockyou.txt -o cracked.txt
```

So let's go over each of the flags above:
- '-m 0': -m is used to indicate what type of hash you are cracking, in the command we ran above we could see that md5 was 0.
- '-a 0': -a specifies what attack method you are wanting to use, 0 indicates we want to do a dictionary attack.
- '482c811da5d5b4bc6d497ffa98491e38':  We then need to specify the hash, make sure you either point to a text file or enclose your hash in quotes.
- /usr/share/wordlists/rockyou.txt:  Then we point to our dictionary file, all Kali wordlists can be found in /usr/share/wordlists/.
- '-o cracked.txt':  Lastly, the -o flag indicates we want to output the results to a file (in this case cracked.txt).

And when we run the command we get the below output:

![Hashcat](https://github.com/user-attachments/assets/4d48b1f7-d2c5-4e77-acef-70438b827bad)

This password was so early in the wordlist that it barely ran for more than a few seconds!  More complicated passwords that include salts can take a very long time to crack however.

When we open the cracked.txt file we get the below password:

``` bash
└─$ cat cracked.txt
482c811da5d5b4bc6d497ffa98491e38:password123
```

Looks like the password is 'password123', very original!  Let's plug that into the server now:

![Second Hash](https://github.com/user-attachments/assets/622b6b22-1340-49e2-a66b-0f5ffdda7fa3)

Another hash! Let's run through the process again:

![SHA1](https://github.com/user-attachments/assets/1927e269-8fb8-453c-b0db-84af27c9139b)

It appears to be a SHA1 hash, let's run it through hashcat again:

``` bash
hashcat -m 100 -a 0 'b7a875fc1ea228b9061041b7cec4bd3c52ab3ce3' /usr/share/wordlists/rockyou.txt -o cracked.txt
```

Gives us the password 'letmein', let's try that!

You can probably guess what happens next, we get another hash!  No more hints, you can figure it out I'm sure.  We eventually crack that last hash, plug it in, and we get the flag!  Nice!
