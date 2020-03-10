'''
Task
Given an array, A, of N integers, print A's elements in reverse order as a single line of space-separated numbers.
'''


n = int(input())

arr = list(map(int, input().rstrip().split()))

reversed_arr = arr[:]

for i in range(n):
    if i>=n-i-1:
        break
    reversed_arr[i], reversed_arr[n-i-1] = reversed_arr[n-i-1], reversed_arr[i]

reversed_str = ''
for i in reversed_arr:
    reversed_str += "{} ".format(i)

print(reversed_str)

"""
#alternative
for i in reversed(arr):
    reversed_arr += "{} ".format(i)
print(reversed_arr)
"""

