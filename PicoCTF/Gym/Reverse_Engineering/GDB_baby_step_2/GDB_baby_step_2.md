# GDB Baby Step 2
This was a challenge listed exclusively for the Pico Gym.  It's listed as Medium and categorized as a Reverse Engineering challenge.  
Direct Link:  https://play.picoctf.org/practice/challenge/396

## Description
The Description reads:
> Can you figure out what is in the eax register at the end of the main function?
> Disassemble this.

## Hints
There is one hint:
> You could calculate eax yourself, or you could set a breakpoint for after the calculcation and inspect eax to let the program do the heavy-lifting for you.

# Solving
## My Thoughts
This builds on the previous GDB challenge making things a little more interesting.

## GDB
Let's open GDB and check out the functions and the main again:

``` bash
pwndbg> info functions
All defined functions:

Non-debugging symbols:
0x0000000000401000  _init
0x0000000000401020  _start
0x0000000000401050  _dl_relocate_static_pie
0x0000000000401060  deregister_tm_clones
0x0000000000401090  register_tm_clones
0x00000000004010d0  __do_global_dtors_aux
0x0000000000401100  frame_dummy
0x0000000000401106  main
0x0000000000401150  __libc_csu_init
0x00000000004011c0  __libc_csu_fini
0x00000000004011c8  _fini
pwndbg> disassemble main
Dump of assembler code for function main:
   0x0000000000401106 <+0>:     endbr64
   0x000000000040110a <+4>:     push   rbp
   0x000000000040110b <+5>:     mov    rbp,rsp
   0x000000000040110e <+8>:     mov    DWORD PTR [rbp-0x14],edi
   0x0000000000401111 <+11>:    mov    QWORD PTR [rbp-0x20],rsi
   0x0000000000401115 <+15>:    mov    DWORD PTR [rbp-0x4],0x1e0da
   0x000000000040111c <+22>:    mov    DWORD PTR [rbp-0xc],0x25f
   0x0000000000401123 <+29>:    mov    DWORD PTR [rbp-0x8],0x0
   0x000000000040112a <+36>:    jmp    0x401136 <main+48>
   0x000000000040112c <+38>:    mov    eax,DWORD PTR [rbp-0x8]
   0x000000000040112f <+41>:    add    DWORD PTR [rbp-0x4],eax
   0x0000000000401132 <+44>:    add    DWORD PTR [rbp-0x8],0x1
   0x0000000000401136 <+48>:    mov    eax,DWORD PTR [rbp-0x8]
   0x0000000000401139 <+51>:    cmp    eax,DWORD PTR [rbp-0xc]
   0x000000000040113c <+54>:    jl     0x40112c <main+38>
   0x000000000040113e <+56>:    mov    eax,DWORD PTR [rbp-0x4]
   0x0000000000401141 <+59>:    pop    rbp
   0x0000000000401142 <+60>:    ret
End of assembler dump.
```

A lot more complicated than last time!  It looks like there's some logic going on there but we don't need to spend time figure out what's going on!

We can see that the function returns at 0x0000000000401142, so if we just set a breakpoint there and try to read the value of EAX, we shoudl get our flag:

``` bash
pwndbg> b *0x401142
Breakpoint 1 at 0x401142
pwndbg> run
Starting program: /home/noah/picoctf/gym/binary_exploitation/gdb_baby_2/debugger0_b
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".

Breakpoint 1, 0x0000000000401142 in main ()

pwndbg> print $eax
$1 = 307019
```

Looks like our value should be 307019!  So our flag is picoCTF{307019}!
