'''
Task
Given n names and phone numbers, assemble a phone book that maps friends' names to their respective phone numbers.
You will then be given an unknown number of names to query your phone book for.
For each name queried, print the associated entry from your phone book on a new line in the form name=phoneNumber;
if an entry for name is not found, print Not found instead.

Sample Input
3
sam 99912222
tom 11122222
harry 12299933
sam
edward
harry

Sample Output
sam=99912222
Not found
harry=12299933
'''


import sys

input_data = sys.stdin.readlines()

phonebook = dict()
count = int(input_data[0])
for i in range(1,count+1):
    current = input_data[i].rstrip().split()
    phonebook[''.join(current[0])] = ''.join(current[1])

for i in range(count+1, len(input_data)):
    name = input_data[i].rstrip()
    if name in phonebook.keys():
        print('{}={}'.format(name, phonebook[name]))
    else:
        print('Not found')
