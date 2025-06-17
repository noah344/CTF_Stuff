# Bit-O-Asm-4
This was a challenge listed exclusively for the Pico Gym.  It's listed as Medium and categorized as a Reverse Engineering challenge.  
Direct Link:  https://play.picoctf.org/practice/challenge/394

## Description
The Description reads:
> Can you figure out what is in the eax register?

## Hints
There are two hints:
> Don't tell anyone I told you this, but you can solve this problem without understanding the compare/jump relationship.
> Of course, if you're really good, you'll only need one attempt to solve this problem.

# Solving
## My Thoughts
A nice intro to assembly.

## Reading the Assembly
Let's pull down the file and read it:

``` bash
┌──(root㉿kali)-[/home/noah/picoctf/gym/Bit-O-Asm-4]
└─# wget https://artifacts.picoctf.net/c/511/disassembler-dump0_d.txt -q; cat *
<+0>:     endbr64
<+4>:     push   rbp
<+5>:     mov    rbp,rsp
<+8>:     mov    DWORD PTR [rbp-0x14],edi
<+11>:    mov    QWORD PTR [rbp-0x20],rsi
<+15>:    mov    DWORD PTR [rbp-0x4],0x9fe1a
<+22>:    cmp    DWORD PTR [rbp-0x4],0x2710
<+29>:    jle    0x55555555514e <main+37>
<+31>:    sub    DWORD PTR [rbp-0x4],0x65
<+35>:    jmp    0x555555555152 <main+41>
<+37>:    add    DWORD PTR [rbp-0x4],0x65
<+41>:    mov    eax,DWORD PTR [rbp-0x4]
<+44>:    pop    rbp
<+45>:    ret
```

Now let's comment it out a bit:

```
<+0>:     endbr64 - Not Important
<+4>:     push   rbp - Not Important
<+5>:     mov    rbp,rsp - Not Important
<+8>:     mov    DWORD PTR [rbp-0x14],edi - Not Important
<+11>:    mov    QWORD PTR [rbp-0x20],rsi - Not Important
<+15>:    mov    DWORD PTR [rbp-0x4],0x9fe1a - Sets the value of pointer rbp-0x4 to 0x9fe1a
<+22>:    cmp    DWORD PTR [rbp-0x4],0x2710 - Compares the value stored in pointer rbp-0x4 with 0x2710
<+29>:    jle    0x55555555514e <main+37> - If, in the above comparison, pointer rbp-0x4 is less than or equal to 0x2710, then jump to +37
<+31>:    sub    DWORD PTR [rbp-0x4],0x65 - Otherwise, subtract 0x65 from the value stored in pointer rbp-0x4
<+35>:    jmp    0x555555555152 <main+41> - and jump to +41.
<+37>:    add    DWORD PTR [rbp-0x4],0x65 - Adds 0x65 to the value stored in pointer rbp-0x4
<+41>:    mov    eax,DWORD PTR [rbp-0x4] - Sets eax to equal the value of pointer rbp-0x4
<+44>:    pop    rbp
<+45>:    ret
```

So let's run through it:

1. rbp-0x4 = 0x9fe1a
2. 0x9fe1a <= 0x2710 = False, skip the jump
3. rbp-0x4 - 0x65 = 0x9fe1a - 0x65 = 0x9FDB5
4. Jump to +41
5. eax = rbp-0x4 = 0x9FDB5 = 654773

So our flag is picoCTF{654773}!
