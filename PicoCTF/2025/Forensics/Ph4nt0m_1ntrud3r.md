# Ph4nt0m 1ntrud3r
This was a challenge from PicoCTF 2025.  It's listed as easy and categorized as a Forensics challenge.

## Description
The Description reads:
> A digital ghost has breached my defenses, and my sensitive data has been stolen!  
> 😱💻 Your mission is to uncover how this phantom intruder infiltrated my system and retrieve the hidden flag.  
> To solve this challenge, you'll need to analyze the provided PCAP file and track down the attack method.  
> The attacker has cleverly concealed his moves in well timely manner.  
> Dive into the network traffic, apply the right filters and show off your forensic prowess and unmask the digital intruder!  

## Hints
There are three hints that read:
> Filter your packets to narrow down your search.  

> Attacks were done in timely manner.  

and
> Time is essential

# Solving
## My Thoughts
I was really happy to have a pcap analysis challenge in this CTF, I love looking at packets.  I was pretty disappointed with the quality of this one however and don't think it really showed off Wireshark and it's full capabilities well.  The hints were also way too good and basically pointed directly to the solution.

## What's a PCAP?
PCAPs are essentially records of all packets that have crossed a specific network interface.  You can save the capture to a file and then go back and review them all to see what's going on.

PCAPs can show you EXACTLY what's going on within your network, down to the bits and bytes.

## Wireshark

Let's import the pcap into wireshark:

![Wireshark](https://github.com/user-attachments/assets/9f1c7a22-c438-4f38-a67a-1c5c68f5409e)

Ok, immediately we can see that the timing doesn't match the order the packets come in.  Wireshark does it's best to interpret the data it's given, but it's not always 100% perfect, which is where the human factor comes in.  The packets were crafted to make them be displayed out of order by default in wireshark.  You can see this based on the timing and the "Stream Index" value.

We can instead force wireshark to sort by Time which will give us the actual timing of when things arrived:

![Timing](https://github.com/user-attachments/assets/6cfe1c8b-af4c-4d46-9933-56d1c010bd64)

That's a little better, now let's look at the individual packets.  Scrolling through, we can see that there's some interesting values in the payload fields of a few packets:

![Payload](https://github.com/user-attachments/assets/111448bb-4858-4ea5-a765-80f9d886ba42)

If you aren't familiar, base64 encoded text will USUALLY end in ==, so let's filter out all packets that don't have ==:

![Base64](https://github.com/user-attachments/assets/a88b65da-677e-44be-806f-023b489cf072)

Ok, now we're cooking, let's go through each payload and decode it:

```
cGljb0NURg== - picoCTF
ezF0X3c0cw== - {1t_w4s
bnRfdGg0dA== - nt_th4t
XzM0c3lfdA== - _34sy_t
YmhfNHJfYQ== - bh_4r_a
ZjE2MDk4MA== - f160980
fQ==         - }
picoCTF{1t_w4snt_th4t_34sy_tbh_4r_af160980}
```

Flag acquired!
