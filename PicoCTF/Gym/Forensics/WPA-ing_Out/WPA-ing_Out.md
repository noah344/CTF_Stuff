# WPA-ing Out
This was a challenge listed exclusively for the Pico Gym.  It's listed as Medium and categorized as a Forensics challenge.  
Direct Link:  https://play.picoctf.org/practice/challenge/237

## Description
The Description reads:
> I thought that my password was super-secret, but it turns out that passwords passed over the AIR can be CRACKED, especially if I used the same wireless network password as one in the rockyou.txt credential dump.  
> Use this 'pcap file' and the rockyou wordlist. The flag should be entered in the picoCTF{XXXXXX} format.

## Hints
There are two hints:
> Finding the IEEE 802.11 wireless protocol used in the wireless traffic packet capture is easier with wireshark, the JAWS of the network.
> Aircrack-ng can make a pcap file catch big air...and crack a password.

# Solving
## My Thoughts
This is a pretty good intro challenge to the aircrack suite.

# Aircrack
The description tells us....pretty much exactly what we need to do to solve the challenge.

Let's first download the pcap:

``` bash
┌──(root㉿kali)-[~]
└─# wget https://artifacts.picoctf.net/c/41/wpa-ing_out.pcap -q; ls
wpa-ing_out.pcap
```

Now we simply have to load it up in aircrack-ng and supply it with the rockyou wordlist:

<img width="1612" height="973" alt="image" src="https://github.com/user-attachments/assets/6a883726-f73d-49b1-881c-3bd07103367e" />

And there's our flag!
