# GDB Baby Step 1
This was a challenge listed exclusively for the Pico Gym.  It's listed as Medium and categorized as a Reverse Engineering challenge.  
Direct Link:  https://play.picoctf.org/practice/challenge/395

## Description
The Description reads:
> Can you figure out what is in the eax register at the end of the main function?
> Disassemble this.

## Hints
There are two hints:
> gdb is a very good debugger to use for this problem and many others!
> main is actually a recognized symbol that can be used with gdb commands.

# Solving
## My Thoughts
A nice intro to GDB.

## GDB
Let's go ahead and run our program through gdb (or pwndbg in my case) and check on the functions in the program:

``` bash
┌──(kali㉿kali)-[~/picoctf/gym/binary_exploitation/gdb_baby_1]
└─$ pwndbg debugger0_a
pwndbg> info functions
All defined functions:

Non-debugging symbols:
0x0000000000001000  _init
0x0000000000001030  __cxa_finalize@plt
0x0000000000001040  _start
0x0000000000001070  deregister_tm_clones
0x00000000000010a0  register_tm_clones
0x00000000000010e0  __do_global_dtors_aux
0x0000000000001120  frame_dummy
0x0000000000001129  main
0x0000000000001140  __libc_csu_init
0x00000000000011b0  __libc_csu_fini
0x00000000000011b8  _fini
```

Looks like the only function of any interest (also indicated by the description and hints) is the main function.  

The description also indicates that we should be grabbing the value of EAX at the end of main, but what is EAX?  EAX is generally where the return value of a function is stored.

Let's use GDB to disassemble the main function:

``` bash
pwndbg> disassemble main
Dump of assembler code for function main:
   0x0000000000001129 <+0>:     endbr64
   0x000000000000112d <+4>:     push   rbp
   0x000000000000112e <+5>:     mov    rbp,rsp
   0x0000000000001131 <+8>:     mov    DWORD PTR [rbp-0x4],edi
   0x0000000000001134 <+11>:    mov    QWORD PTR [rbp-0x10],rsi
   0x0000000000001138 <+15>:    mov    eax,0x86342
   0x000000000000113d <+20>:    pop    rbp
   0x000000000000113e <+21>:    ret
End of assembler dump.
```

We can see above that the eax value (located at 0x0000000000001138) contains the value 0x86342.  The instructions say to convert the hex to decimal so let's do that:

``` bash
┌──(kali㉿kali)-[~/picoctf/gym/binary_exploitation/gdb_baby_1]
└─$ python -c 'print(int(0x86342))'
549698
```

So our flag is picoCTF{549698}, nice!
