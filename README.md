# redpwnCTF-coffer-overflow-0-coffer-overflow-1-coffer-overflow-2

These were most simple and first 3 questions of redpwnCTF

''' ALL of them have no security functionality enabled '''

Coffer-Overflow-0

This question is simple, the variable code is first element to be overflown after buffer overflow.
So,we just need to supply more input than what is required to overflow the stack

To overflow rip, we need rbp+8 bytes= 16+8 input bytes
Adding anything to the stack, will cause buffer-overflow and overwrite the first variable named ''code''

Coffer-Overflow-1

Similar to previous one, just difference being the variable "code" has to be replaced by value 0xdeadbeef.
Eaxctly the same procedure, just add the value that we want to write after 24 bytes(rbp + 8)

COffer-Overflow-2

Again the same, just we need to add the value of function binFunction() after buffer overflow

gdb-peda$ info functions
binFunction 0x4006e7

Just add that value after overflow.
