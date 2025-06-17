# Bit-O-Asm-1
This was a challenge listed exclusively for the Pico Gym.  It's listed as Medium and categorized as a Reverse Engineering challenge.  
Direct Link:  https://play.picoctf.org/practice/challenge/391

## Description
The Description reads:
> Can you figure out what is in the eax register?

## Hints
There is one hint:
> As with most assembly, there is a lot of noise in the instruction dump. Find the one line that pertains to this question and don't second guess yourself!

# Solving
## My Thoughts
A nice intro to assembly.

## Reading the Assembly
We can download the file using wget:

``` bash
┌──(root㉿kali)-[/home/noah/picoctf/gym/Bit-O-Asm-1]
└─# wget https://artifacts.picoctf.net/c/509/disassembler-dump0_a.txt -q; ls
disassembler-dump0_a.txt
```

Now let's take a look at the file:

```
<+0>:     endbr64
<+4>:     push   rbp
<+5>:     mov    rbp,rsp
<+8>:     mov    DWORD PTR [rbp-0x4],edi
<+11>:    mov    QWORD PTR [rbp-0x10],rsi
<+15>:    mov    eax,0x30
<+20>:    pop    rbp
<+21>:    ret
```

We are meant to be looking for what's currently in the eax register.  The line labelled as +15 seems to indicate that we are moving the hex value of 0x30 into eax.

So let's give that a try, 0x30 in decimal is 48 so our flag would be:  picoCTF{48}

Sure enough that worked!
