# Bit-O-Asm-3
This was a challenge listed exclusively for the Pico Gym.  It's listed as Medium and categorized as a Reverse Engineering challenge.  
Direct Link:  https://play.picoctf.org/practice/challenge/393

## Description
The Description reads:
> Can you figure out what is in the eax register?

## Hints
There is one hint:
> Not everything in this disassembly listing is optimal.

# Solving
## My Thoughts
A nice intro to assembly.

## Reading the Assembly
Let's pull it down and read it again:

``` bash
┌──(root㉿kali)-[/home/noah/picoctf/gym/Bit-O-Asm-3]
└─# wget https://artifacts.picoctf.net/c/530/disassembler-dump0_c.txt -q; cat *
<+0>:     endbr64
<+4>:     push   rbp
<+5>:     mov    rbp,rsp
<+8>:     mov    DWORD PTR [rbp-0x14],edi
<+11>:    mov    QWORD PTR [rbp-0x20],rsi
<+15>:    mov    DWORD PTR [rbp-0xc],0x9fe1a
<+22>:    mov    DWORD PTR [rbp-0x8],0x4
<+29>:    mov    eax,DWORD PTR [rbp-0xc]
<+32>:    imul   eax,DWORD PTR [rbp-0x8]
<+36>:    add    eax,0x1f5
<+41>:    mov    DWORD PTR [rbp-0x4],eax
<+44>:    mov    eax,DWORD PTR [rbp-0x4]
<+47>:    pop    rbp
<+48>:    ret
```

Below is my commented version of the above:

```
<+0>:     endbr64 - Not Important
<+4>:     push   rbp - Not Important
<+5>:     mov    rbp,rsp - Not Important
<+8>:     mov    DWORD PTR [rbp-0x14],edi - Not Important
<+11>:    mov    QWORD PTR [rbp-0x20],rsi - Not Important
<+15>:    mov    DWORD PTR [rbp-0xc],0x9fe1a - pointer rbp-0xc is assigned the value 0x9fe1a
<+22>:    mov    DWORD PTR [rbp-0x8],0x4 - pointer rbp-0x8 is assigned the value 0x4
<+29>:    mov    eax,DWORD PTR [rbp-0xc] - eax is assigned the value stored in pointer rbp-0xc
<+32>:    imul   eax,DWORD PTR [rbp-0x8] - the value of eax is multiplied by the value stored in pointer rbp-0x8
<+36>:    add    eax,0x1f5 - the hex value 0x1f5 is added to the value stored in eax
<+41>:    mov    DWORD PTR [rbp-0x4],eax - pointer rbp-0x4 is assigned the value of eax
<+44>:    mov    eax,DWORD PTR [rbp-0x4] - eax is assigned the pointer rbp-0x4
<+47>:    pop    rbp
<+48>:    ret
```

So, let's run through it:

1. rbp-0xc = 0x9fe1a
2. rbp-0x8 = 0x4
3. eax = rbp-0xc = 0x9fe1a
4. eax * 0x8 = 0x9fe1a * 0x4 = 0x27F868
5. eax + 0x1f5 = 0x27F868 + 0x1F5 = 0x27FA5D
6. rbp-0x4 = eax
7. eax = rbp-0x4

So our flag should be picoCTF{2619997}!
