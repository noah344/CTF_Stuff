# Repetitions
This was a challenge listed in PicoCTF 2023.  It's listed as Easy and categorized as a General Skills challenge.

## Description
The Description reads:
> Can you make sense of this file?

## Hints
There is a single hint that reads:
> Multiple decoding is always good.

# Solving
## My Thoughts
A fairly basic challenge, not really sure that it adds any value other than to understand that you can encode things multiple times.

## Base64
I've explained base64 in other challenges before, essentially it's a way of encoding text.  Base64 encoded text will usually look like a series of alphanumeric characters sometimes followed by one or two equals signs.

When we take a look at the file we downloaded with cat, we can see that the text is base64 encoded:

``` bash
└─$ cat enc_flag
VmpGU1EyRXlUWGxTYmxKVVYwZFNWbGxyV21GV1JteDBUbFpPYWxKdFVsaFpWVlUxWVZaS1ZWWnVh
RmRXZWtab1dWWmtSMk5yTlZWWApiVVpUVm10d1VWZFdVa2RpYlZaWFZtNVdVZ3BpU0VKeldWUkNk
MlZXVlhoWGJYQk9VbFJXU0ZkcVRuTldaM0JZVWpGS2VWWkdaSGRXCk1sWnpWV3hhVm1KRk5XOVVW
VkpEVGxaYVdFMVhSbFZrTTBKVVZXcE9VazFXV2toT1dHUllDbUY2UWpSWk1GWlhWa2RHZEdWRlZs
aGkKYlRrelZERldUMkpzUWxWTlJYTkxDZz09Cg==
```

We can use a builtin linux tool to decode it by first reading in the file, then piping the output to base64 --decode as shown below:

``` bash
└─$ cat enc_flag | base64 --decode
VjFSQ2EyTXlSblJUV0dSVllrWmFWRmx0TlZOalJtUlhZVVU1YVZKVVZuaFdWekZoWVZkR2NrNVVX
bUZTVmtwUVdWUkdibVZXVm5WUgpiSEJzWVRCd2VWVXhXbXBOUlRWSFdqTnNWZ3BYUjFKeVZGZHdW
MlZzVWxaVmJFNW9UVVJDTlZaWE1XRlVkM0JUVWpOUk1WWkhOWGRYCmF6QjRZMFZXVkdGdGVFVlhi
bTkzVDFWT2JsQlVNRXNLCg==
```

The name of the challenge makes sense now! We've got text that's been encoded with base64 multiple times, lets go through until we get the flag by repeatedly piping the output:

``` bash
└─$ cat enc_flag| base64 --decode | base64 --decode | base64 --decode | base64 --decode | base64 --decode | base64 --decode
picoCTF{base64_n3st3d_dic0d!n8_d0wnl04d3d_492767d2}
```

There we go, flag acquired!
