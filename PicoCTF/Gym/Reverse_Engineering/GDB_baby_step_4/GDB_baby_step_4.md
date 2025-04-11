# GDB Baby Step 4
This was a challenge listed exclusively for the Pico Gym.  It's listed as Medium and categorized as a Reverse Engineering challenge.  
Direct Link:  https://play.picoctf.org/practice/challenge/398

## Description
The Description reads:
> main calls a function that multiplies eax by a constant.
> The flag for this challenge is that constant in decimal base.
> If the constant you find is 0x1000, the flag will be picoCTF{4096}.
> Debug this.

## Hints
There is one hint:
> A function can be referenced by either its name or its starting address in gdb.

# Solving
## My Thoughts
This one was pretty simple, I'm not certain that it built much on the other challenges and definitely should not have been a medium.

## GDB
Let's do the same as before and get a list of functions:

``` bash
pwndbg> info function
All defined functions:

Non-debugging symbols:
0x0000000000401000  _init
0x0000000000401020  _start
0x0000000000401050  _dl_relocate_static_pie
0x0000000000401060  deregister_tm_clones
0x0000000000401090  register_tm_clones
0x00000000004010d0  __do_global_dtors_aux
0x0000000000401100  frame_dummy
0x0000000000401106  func1
0x000000000040111c  main
0x0000000000401150  __libc_csu_init
0x00000000004011c0  __libc_csu_fini
0x00000000004011c8  _fini
```

There's the new function the description mentioned, func1.  Let's dissassemble that:

``` bash
pwndbg> disassemble func1
Dump of assembler code for function func1:
   0x0000000000401106 <+0>:     endbr64
   0x000000000040110a <+4>:     push   rbp
   0x000000000040110b <+5>:     mov    rbp,rsp
   0x000000000040110e <+8>:     mov    DWORD PTR [rbp-0x4],edi
   0x0000000000401111 <+11>:    mov    eax,DWORD PTR [rbp-0x4]
   0x0000000000401114 <+14>:    imul   eax,eax,0x3269
   0x000000000040111a <+20>:    pop    rbp
   0x000000000040111b <+21>:    ret
End of assembler dump.
```

Ok, so it looks like the constant that eax is multiplied by is 0x3269.  Let's convert that to decimal:

``` bash
┌──(kali㉿kali)-[~/picoctf/gym/binary_exploitation/gdb_baby_4]
└─$ python -c 'print(int(0x3269))'
12905
```

Ok, so our flag is picoCTF{12905}! Nice!
