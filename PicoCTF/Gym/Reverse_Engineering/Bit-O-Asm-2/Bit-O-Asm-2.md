# Bit-O-Asm-2
This was a challenge listed exclusively for the Pico Gym.  It's listed as Medium and categorized as a Reverse Engineering challenge.  
Direct Link:  https://play.picoctf.org/practice/challenge/392

## Description
The Description reads:
> Can you figure out what is in the eax register?

## Hints
There is one hint:
> PTR's or 'pointers', reference a location in memory where values can be stored.

# Solving
## My Thoughts
A nice intro to assembly.

## Reading the Assembly
We can download and read the file like so:

``` bash
┌──(root㉿kali)-[/home/noah/picoctf/gym/Bit-O-Asm-2]
└─# wget https://artifacts.picoctf.net/c/510/disassembler-dump0_b.txt -q; cat *
<+0>:     endbr64
<+4>:     push   rbp
<+5>:     mov    rbp,rsp
<+8>:     mov    DWORD PTR [rbp-0x14],edi
<+11>:    mov    QWORD PTR [rbp-0x20],rsi
<+15>:    mov    DWORD PTR [rbp-0x4],0x9fe1a
<+22>:    mov    eax,DWORD PTR [rbp-0x4]
<+25>:    pop    rbp
<+26>:    ret
```

Once again we are looking for the eax register.  We can see in this case that on +22, eax is set to a DWORD pointer identified by rbp-0x4.

We can see on +15 that the rbp-0x4 dword pointer is set to 0x9fe1a which is equal to 654874 in decimal, so our flag is:  picoCTF{654874}.
