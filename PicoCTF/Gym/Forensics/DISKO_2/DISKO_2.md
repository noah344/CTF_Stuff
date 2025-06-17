# DISKO 2
This was a challenge listed exclusively for the Pico Gym.  It's listed as Medium and categorized as a Forensics challenge.  
Direct Link:  https://play.picoctf.org/practice/challenge/506

## Description
The Description reads:
> Can you find the flag in this disk image? The right one is Linux! One wrong step and its all gone!

## Hints
There is one hint:
> How can you extract/isolate a partition?

# Solving
## My Thoughts
This one was interesting, learned a little more about mounting on Linux.

## Mounting the File
We can download the dd image to our machine again using wget and decompress it using gzip:

``` bash
┌──(root㉿kali)-[/home/noah/picoctf/gym/DISKO_2]
└─# wget https://artifacts.picoctf.net/c/540/disko-2.dd.gz -q; gunzip ./*; ls
disko-2.dd
```

Let's run strings and grep for pico again and see what we get:

``` bash
┌──(root㉿kali)-[/home/noah/picoctf/gym/DISKO_2]
└─# strings disko-2.dd | grep picoCTF{
picoCTF{4_P4Rt_1t_i5_c03b93aa}
picoCTF{4_P4Rt_1t_i5_aa9cb033}
picoCTF{4_P4Rt_1t_i5_30ac9ba3}
picoCTF{4_P4Rt_1t_i5_03cba9a3}
picoCTF{4_P4Rt_1t_i5_039aca3b}
picoCTF{4_P4Rt_1t_i5_30ca93ba}
picoCTF{4_P4Rt_1t_i5_9c3a3a0b}
picoCTF{4_P4Rt_1t_i5_3a9ab3c0}
picoCTF{4_P4Rt_1t_i5_bc93aa30}
picoCTF{4_P4Rt_1t_i5_3aba039c}
picoCTF{4_P4Rt_1t_i5_3a3cba09}
picoCTF{4_P4Rt_1t_i5_a3c9ba30}
picoCTF{4_P4Rt_1t_i5_339b0aca}
picoCTF{4_P4Rt_1t_i5_a0bac933}
```

Lots of junk this time, the description indicated that "the right one is Linux", so let's look closer at the file using the file command:

``` bash
┌──(root㉿kali)-[/home/noah/picoctf/gym/DISKO_2]
└─# file disko-2.dd
disko-2.dd: DOS/MBR boot sector; partition 1 : ID=0x83, start-CHS (0x0,32,33), end-CHS (0x3,80,13), startsector 2048, 51200 sectors; partition 2 : ID=0xb, start-CHS (0x3,80,14), end-CHS (0x7,100,29), startsector 53248, 65536 sectors
```

Interesting, looks like there are two different partitions.  So how would we mount a specific one?

## Mounting a Specific Partition
[This](https://superuser.com/questions/117136/how-can-i-mount-a-partition-from-dd-created-image-of-a-block-device-e-g-hdd-u) stackexchange page was extremely helpful.

We can use a tool called losetup to automatically setup loopback devices for each partition:

``` bash
┌──(root㉿kali)-[/home/noah/picoctf/gym/DISKO_2]
└─# losetup --partscan --find --show disko-2.dd
/dev/loop0
```

We can then check our mounts:

``` bash
┌──(root㉿kali)-[/home/noah/picoctf/gym/DISKO_2]
└─# fdisk -l
Disk /dev/loop0: 100 MiB, 104857600 bytes, 204800 sectors
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disklabel type: dos
Disk identifier: 0x8ef8eaee

Device       Boot Start    End Sectors Size Id Type
/dev/loop0p1       2048  53247   51200  25M 83 Linux
/dev/loop0p2      53248 118783   65536  32M  b W95 FAT32
```

Sure enough, we've got two partitions.  Let's go to that loop device and run our strings command again:

``` bash
┌──(root㉿kali)-[/home/noah/picoctf/gym/DISKO_2]
└─# strings /dev/loop0p1| grep picoCTF
picoCTF{4_P4Rt_1t_i5_a93c3ba0}
```

Look, only one flag this time! And that one appears to be the right one! Nice!
