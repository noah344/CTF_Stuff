# DISKO 3
This was a challenge listed exclusively for the Pico Gym.  It's listed as Medium and categorized as a Forensics challenge.  
Direct Link:  https://play.picoctf.org/practice/challenge/507

## Description
The Description reads:
> Can you find the flag in this disk image? This time, its not as plain as you think it is!

## Hints
There is one hint:
> How will you search and extract files in a partition?

# Solving
## My Thoughts
This one was disappointing.  There was nothing new or challenging about this.

## Mounting the File
We can download the dd image to our machine again using wget and decompress it using gzip:

``` bash
┌──(noah㉿kali)-[~/picoctf/gym/DISKO_3]
└─$ wget https://artifacts.picoctf.net/c/542/disko-3.dd.gz; gunzip ./*; ls
disko-3.dd
```

Let's run strings and grep for pico again and see what we get:

``` bash
┌──(noah㉿kali)-[~/picoctf/gym/DISKO_3]
└─$ strings disko-3.dd | grep pico
pico desta partici
Description-it.UTF-8: Utilizzo tipico di questa partizione:
pico desta parti
Description-it.UTF-8: Utilizzo tipico:
pico:
Aug 30 01:59:37 debootstrap: update-alternatives: using /bin/nano to provide /usr/bin/pico (pico) in auto mode
Aug 30 02:00:42 in-target:   mailx | mailutils snmptrapd libttspico-utils espeak mbrola
MESSAGE=[system] Activating via systemd: service name='org.bluez' unit='dbus-org.bluez.service' requested by ':1.81' (uid=1000 pid=12105 comm="/usr/share/code/code Desktop/picoctf-2025")
MESSAGE=[system] Activating via systemd: service name='org.bluez' unit='dbus-org.bluez.service' requested by ':1.66' (uid=1000 pid=43129 comm="/usr/share/code/code Desktop/picoctf-2025")
MESSAGE=[system] Activating via systemd: service name='org.bluez' unit='dbus-org.bluez.service' requested by ':1.65' (uid=1000 pid=2141 comm="/usr/share/code/code Desktop/picoctf-2025")
MESSAGE=[system] Activating via systemd: service name='org.bluez' unit='dbus-org.bluez.service' requested by ':1.65' (uid=1000 pid=2584 comm="/usr/share/code/code Desktop/picoctf-2025")
```

Some weird messages in there this time, let's remember that directory.  Let's see what kind of file it is:

``` bash
┌──(noah㉿kali)-[~/picoctf/gym/DISKO_3]
└─$ file disko-3.dd
disko-3.dd: DOS/MBR boot sector, code offset 0x58+2, OEM-ID "mkfs.fat", Media descriptor 0xf8, sectors/track 32, heads 8, sectors 204800 (volumes > 32 MB), FAT (32 bit), sectors/FAT 1576, serial number 0x49838d0b, unlabeled
```

This one's definitely different than the last one.  Looks like it might be FAT32 formatted?

Let's try to mount it.

## Mounting a Specific Partition
We can just simply mount it with the following command (as root):

``` bash
┌──(root㉿kali)-[/home/noah/picoctf/gym/DISKO_3]
└─# mount disko-3.dd /media/stuff
```

And now lets go poke around:

``` bash
┌──(root㉿kali)-[/home/noah/picoctf/gym/DISKO_3]
└─# cd /media/stuff

┌──(root㉿kali)-[/media/stuff]
└─# ls
log

┌──(root㉿kali)-[/media/stuff]
└─# cd log

┌──(root㉿kali)-[/media/stuff/log]
└─# ls
Xorg.0.log             boot.log.1  dpkg.log.2.gz  installer      macchanger.log.4.gz  sysstat               vmware-network.6.log     vmware-vmsvc-root.3.log
Xorg.0.log.old         boot.log.5  dpkg.log.4.gz  journal        mysql                vmware-network.1.log  vmware-network.7.log     vmware-vmsvc-root.log
alternatives.log       boot.log.6  dpkg.log.5.gz  kern.log.3.gz  private              vmware-network.2.log  vmware-network.8.log     vmware-vmtoolsd-root.log
alternatives.log.2.gz  daemon.log  faillog        kern.log.4.gz  stunnel4             vmware-network.3.log  vmware-network.log       wtmp
apt                    debug       flag.gz        lastlog        syslog.3.gz          vmware-network.4.log  vmware-vmsvc-root.1.log
boot.log               dpkg.log.1  inetsim        lightdm        syslog.4.gz          vmware-network.5.log  vmware-vmsvc-root.2.log
```

There's an interesting file in here called 'flag.gz', let's grab that and extract it:

``` bash
┌──(root㉿kali)-[/media/stuff/log]
└─# gunzip flag.gz

┌──(root㉿kali)-[/media/stuff/log]
└─# ls
Xorg.0.log             boot.log.1  dpkg.log.2.gz  installer      macchanger.log.4.gz  sysstat               vmware-network.6.log     vmware-vmsvc-root.3.log
Xorg.0.log.old         boot.log.5  dpkg.log.4.gz  journal        mysql                vmware-network.1.log  vmware-network.7.log     vmware-vmsvc-root.log
alternatives.log       boot.log.6  dpkg.log.5.gz  kern.log.3.gz  private              vmware-network.2.log  vmware-network.8.log     vmware-vmtoolsd-root.log
alternatives.log.2.gz  daemon.log  faillog        kern.log.4.gz  stunnel4             vmware-network.3.log  vmware-network.log       wtmp
apt                    debug       flag           lastlog        syslog.3.gz          vmware-network.4.log  vmware-vmsvc-root.1.log
boot.log               dpkg.log.1  inetsim        lightdm        syslog.4.gz          vmware-network.5.log  vmware-vmsvc-root.2.log

┌──(root㉿kali)-[/media/stuff/log]
└─# cat flag
Here is your flag
picoCTF{n3v3r_z1p_2_h1d3_7e0a17da}
```

Sure enough, we got our flag!
