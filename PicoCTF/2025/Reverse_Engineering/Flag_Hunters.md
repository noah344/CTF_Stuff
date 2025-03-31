# Flag Hunters
This challenge was for PicoCTF 2025. It's listed as easy and categorized as a Reverse Engineering challenge.

## Description
The Description reads:
> Lyrics jump from verses to the refrain kind of like a subroutine call.  
> There's a hidden refrain this program doesn't print by default.  
> Can you get it to print it?  
> There might be something in it for you.

## Hints
There are three hints that read:
> This program can easily get into undefined states. Don't be shy about Ctrl-C.

> Unsanitized user input is always good, right?

and
> Is there any syntax that is ripe for subversion?

# Solving
# My Thoughts
This one was ok, I found it pretty annoying that I got stuck on a very minor issue for a while which probably brings down my rating of it.

## Running the Program
I started by simply downloading the python script and running it locally to see what happened, it essentially just prints out a bunch of lyrics and then takes user input to print out some additional lyrics, nothing too interesting:

![lyric_reader](https://github.com/user-attachments/assets/98cc3909-d24c-48c9-9bf5-3021fd9fd1e8)

Let's take a look at the source code, immediately at the top there's a string named 'secret_intro' that appears as though it would print out the flag when it's printed:

``` python
# Read in flag from file
flag = open('flag.txt', 'r').read()

secret_intro = \
'''Pico warriors rising, puzzles laid bare,
Solving each challenge with precision and flair.
With unity and skill, flags we deliver,
The ether’s ours to conquer, '''\
+ flag + '\n'
```
The secret_intro and the rest of the lyrics are added to a string named 'song_flag_hunters', with the secret intro in front.  Each other section of lyrics starts with some text in brackets like this:  '[REFRAIN]'.  Sometimes there are also breaks that looks like this:  'REFRAIN;'.  This will make a little more sense later.

We then get to the 'reader' function, the full source code is below:

``` python
def reader(song, startLabel):
  lip = 0
  start = 0
  refrain = 0
  refrain_return = 0
  finished = False

  # Get list of lyric lines
  song_lines = song.splitlines()
  
  # Find startLabel, refrain and refrain return
  for i in range(0, len(song_lines)):
    if song_lines[i] == startLabel:
      start = i + 1
    elif song_lines[i] == '[REFRAIN]':
      refrain = i + 1
    elif song_lines[i] == 'RETURN':
      refrain_return = i

  # Print lyrics
  line_count = 0
  lip = start
  while not finished and line_count < MAX_LINES:
    line_count += 1
    for line in song_lines[lip].split(';'):
      if line == '' and song_lines[lip] != '':
        continue
      if line == 'REFRAIN':
        song_lines[refrain_return] = 'RETURN ' + str(lip + 1)
        lip = refrain
      elif re.match(r"CROWD.*", line):
        crowd = input('Crowd: ')
        song_lines[lip] = 'Crowd: ' + crowd
        lip += 1
      elif re.match(r"RETURN [0-9]+", line):
        lip = int(line.split()[1])
      elif line == 'END':
        finished = True
      else:
        print(line, flush=True)
        time.sleep(0.5)
        lip += 1
```
There are two sections in particular that I noticed immediately were interesting.

First was the initiator for the for loop which split the lyrics by the ';' character:

``` python
for line in song_lines[lip].split(';'):
```

The second was an elif section that checked for a regex match to a string that would be 'RETURN x' where x would be a number between 0 and 9.  Based on the lyrics, this elif should never be called:

``` python
elif re.match(r"RETURN [0-9]+", line):
  lip = int(line.split()[1])
```

Another crucial part (that I'm now understanding after the fact), is what exactly 'continue' does in python.  The 'continue' keyword will skip to the next value in the for loop when it's called so, if the below if statement is successful, the 'line' variable will iterate:

``` python
if line == '' and song_lines[lip] != '':
  continue
```

So, if the line it's currently reading is empty, and the line at 'lip' is not empty, it will iterate the value of line immediately.  This is the critical part of it all and how we're going to manipulate the program to do what we want.

Let's start by just putting in ';' along with some random text and see what happens:

![Testing](https://github.com/user-attachments/assets/00785dca-87ed-408e-9313-220c7139ddf4)

Wow, program seems completely messed up now!  Let's try to manipulate that regex now?  Since we want to get to the first set of lines in the lyrics, lets do ';RETURN 0':

![Flag](https://github.com/user-attachments/assets/923405fe-6c80-4929-99ad-bddfaba7221a)

Well, there it is! I was stuck on this for far longer than I should have because I kept entering '; RETURN 0' without realizing.  Like I said this challenge was a little on the disappointing side, I'm never really a fan of programs that are intentionally written out to be confusing as it doesn't really mirror a real world scenario.
