'''
Task
Given an integer, , perform the following conditional actions:
If n is odd, print Weird
If n is even and in the inclusive range of 2 to 5, print Not Weird
If n is even and in the inclusive range of 6 to 20, print Weird
If n is even and greater than 20, print Not Weird
Complete the stub code provided in your editor to print whether or not n is weird.
'''


N = int(input())

if N%2 == 0:
    if N in range(2,6) or N > 20:
        print("Not Weird")
    elif N in range(6,21):
        print("Weird")
else:
    print("Weird")