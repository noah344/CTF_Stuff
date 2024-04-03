import sys
import base64
from cryptography.fernet import Fernet

# This initiates a string that will include the first argument passed by the user (in this case this will be the name of the script).
usage_msg = "Usage: "+ sys.argv[0] +" (-e/-d) [file]"
# This initiates a string that instructs the user on how to use the script.  sys.argv[0] will do the same as above where it'll output the name of the script at that designated spot in the string.
help_msg = usage_msg + "\n" +\
        "Examples:\n" +\
        "  To decrypt a file named 'pole.txt', do: " +\
        "'$ python "+ sys.argv[0] +" -d pole.txt'\n"

# This if statement checks if the user has supplied more than 2 arguments and less than 4 arguments.  For instance, if the user ran the script with "python ende.py wow very cool thumbs up", the script will print the usage info and then exit.
if len(sys.argv) < 2 or len(sys.argv) > 4:
    print(usage_msg)
    sys.exit(1)

# This if statement checks to see if the second (or first depending on how you want to think about it) argument provided by the user is -e.
if sys.argv[1] == "-e":
    # This checks if the number of user arguments is less than 4.
    if len(sys.argv) < 4:
        # if it is, it prompts the user to enter the password.
        sim_sala_bim = input("Please enter the password:")
    # if the number of arguments is 4 though, the user has already provided the password as that 4th argument.  Remember, lists in python start at 0.
    else:
        sim_sala_bim = sys.argv[3]
        
    # so at this point, the string sim_bala_bim, should contain the password the user wants to use.

    # sim_sala_bim.encode() will convert the string into binary.
    # Once that's done, we use the b64encode function from the base64 module to encode the binary as base64, not really sure what it does that but whatever.
    ssb_b64 = base64.b64encode(sim_sala_bim.encode())
    # This is complicated, to understand it you'll need to look into symmetric encryption.  Fernet essentially makes sure that data cannot be read unless the provided key is used to decrypt it.  In this case, we are setting up c as a Fernet object that has taken in ssb_b64 as the key it will use for encryption.
    c = Fernet(ssb_b64)

    # now we read in the file (provided as argument 3 in the user's input) as binary and place the binary data into object f.
    with open(sys.argv[2], "rb") as f:
        # the binary data is then read into the data variable. 
        data = f.read()
        # the data is then encrypted by the key we provided Fernet earlier and placed into the data_c variable.
        data_c = c.encrypt(data)
        # the data_c data is then output but decoded from binary to normal text.
        sys.stdout.write(data_c.decode())

# Ok, in this case the user wants to decrypt the data instead of encrypt.
elif sys.argv[1] == "-d":
    # Same as the above, basically checks if the users already passed the password to the script.
    if len(sys.argv) < 4:
        sim_sala_bim = input("Please enter the password:")
    else:
        sim_sala_bim = sys.argv[3]

    # See above, basically loading the password into Fernet.
    ssb_b64 = base64.b64encode(sim_sala_bim.encode())
    c = Fernet(ssb_b64)

    # Reads the encrypted file into the f object.
    with open(sys.argv[2], "r") as f:
        # Reads the actual data from the f object into the data string.
        data = f.read()
        # Uses fernet and the provided password to decrypt the data once it's been transformed into binary data.
        data_c = c.decrypt(data.encode())
        # Prints the decrypted data to the console.
        sys.stdout.buffer.write(data_c)

# Sets up help output for the user.
elif sys.argv[1] == "-h" or sys.argv[1] == "--help":
    print(help_msg)
    sys.exit(1)

# Error catching.
else:
    print("Unrecognized first argument: "+ sys.argv[1])
    print("Please use '-e', '-d', or '-h'.")
