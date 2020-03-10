'''
Task
Given a string, S, of length N that is indexed from 0 to N-1, print its even-indexed and odd-indexed characters as 2
space-separated strings on a single line (see the Sample below for more detail).
Note:  is considered to be an even index.
'''


import sys

input_data = sys.stdin.readlines()

for i in range(1,len(input_data)):
    even = ''.join([x for index, x in enumerate(input_data[i]) if index%2==0]).rstrip()
    odd = ''.join([x for index, x in enumerate(input_data[i]) if index%2!=0]).rstrip()
    print('{} {}'.format(even, odd))