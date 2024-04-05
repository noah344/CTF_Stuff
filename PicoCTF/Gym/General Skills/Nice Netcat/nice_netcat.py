#! /usr/bin/python
from subprocess import check_output

# check_output will run a linux command within python and save the output to the output variable
output = check_output(["nc", "mercury.picoctf.net", "7449"])

# The output comes out a little wonky because it's in bytecode so first we want to convert it from bytecode to a string.
# After that, we want to split each character off which we can use with split and setting the delimeter as \n which is the unicode character for a newline break.
output = (output.decode()).split("\n")

# Here we initiate a string to hold our decoded output.
decoded = ""
# Now we loop through each character within the output list.
for i in output:
	# I put exception handling here because sometimes the check_output command will catch some extra stuff we don't want.
	# If this wasn't here, the script would error out on any lines that weren't ascii numbers.
	try:
		# Here we just append each decoded character to the decoded string variable.
		# Each value within the output list is actually an integer but typed as a string, so we have to use int to first transform it into a int and then char to convert the ascii code into it's respective character.
		decoded = decoded + chr(int(i))
	except:
		pass

print(decoded)
