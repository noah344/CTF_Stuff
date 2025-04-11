# GDB Baby Step 3
This was a challenge listed exclusively for the Pico Gym.  It's listed as Medium and categorized as a Reverse Engineering challenge.  
Direct Link:  https://play.picoctf.org/practice/challenge/397

## Description
The Description reads:
> Now for something a little different. 0x2262c96b is loaded into memory in the main function.
> Examine byte-wise the memory that the constant is loaded in by using the GDB command x/4xb addr.
> The flag is the four bytes as they are stored in memory.
> If you find the bytes 0x11 0x22 0x33 0x44 in the memory location, your flag would be: picoCTF{0x11223344}.
> Debug this.

## Hints
There are five hints:
> You'll need to breakpoint the instruction after the memory load.
> Use the gdb command x/4xb addr with the memory location as the address addr to examine. GDB manual page.
> Any registers in addr should be prepended with $ like $rbp.
> Don't use square brackets for addr
> What is endianness?

# Solving
## My Thoughts
This one was a little meh, all it really seemed to introduce was the idea of endianness, the answer was in the description as well so...yeah.

## GDB
We should be getting familiar with this process now, let's go ahead and check the functions and disassemble main:

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
0x0000000000401106  main
0x0000000000401130  __libc_csu_init
0x00000000004011a0  __libc_csu_fini
0x00000000004011a8  _fini
pwndbg> disassemble main
Dump of assembler code for function main:
   0x0000000000401106 <+0>:     endbr64
   0x000000000040110a <+4>:     push   rbp
   0x000000000040110b <+5>:     mov    rbp,rsp
   0x000000000040110e <+8>:     mov    DWORD PTR [rbp-0x14],edi
   0x0000000000401111 <+11>:    mov    QWORD PTR [rbp-0x20],rsi
   0x0000000000401115 <+15>:    mov    DWORD PTR [rbp-0x4],0x2262c96b
   0x000000000040111c <+22>:    mov    eax,DWORD PTR [rbp-0x4]
   0x000000000040111f <+25>:    pop    rbp
   0x0000000000401120 <+26>:    ret
End of assembler dump.
```

So our main looks much different once again.  The description instructs us that we should try to get the memory address that the eax value is saved to.

In this case, it appears as though the value 0x2262c96b was saved to the memory location indicated by rbp-0x4.  So how do we figure out where that's at?

## Examine
Using a command 'x' in gdb, we can examine memory locations.  The description specifically wants us to grab 4 bytes of memory from the memory location, let's go over the command it instructs us to use:

x/4xb
- x:  Calls the examine command
- /: Indicates the flags will follow?
- 4: Indicates that we want to examine 4 units of memory.
- x:  Indicates we want the data in hex.
- b:  Indicates that our unit of memory will be bytes.

We then need to provide it with an address to examine, we can actually use the address shown in the dissassembly above (rbp-0x4).  So let's break just after that is set, run the program, and get our data:

``` bash
pwndbg> b *0x40111c
Breakpoint 1 at 0x40111c
pwndbg> run
Starting program: /home/noah/picoctf/gym/binary_exploitation/gdb_baby_3/debugger0_c
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".
Breakpoint 1, 0x000000000040111c in main ()
pwndbg> x/4xb $rbp-0x4
0x7fffffffdecc: 0x6b    0xc9    0x62    0x22
```

Hey! Those hex characters look familiar, we were provided with 0x2262c96b but it seems stored in reverse order as 0x6bc96222? That's because of endianness! Look it up and learn it cause it's important.

Anyways, our flag should be picoCTF{0x6bc96222}!
