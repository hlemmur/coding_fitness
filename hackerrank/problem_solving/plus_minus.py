'''
Given an array of integers, calculate the fractions of its elements that are positive, negative, and are zeros. Print the decimal value of each fraction on a new line.
Note: This challenge introduces precision problems. The test cases are scaled to six decimal places, though answers with absolute error of up to  are acceptable.
For example, given the array  there are  elements, two positive, two negative and one zero. Their ratios would be ,  and . It should be printed as
0.400000
0.400000
0.200000
Function Description
Complete the plusMinus function in the editor below. It should print out the ratio of positive, negative and zero items in the array, each on a separate line rounded to six decimals.
plusMinus has the following parameter(s):
arr: an array of integers
Input Format
The first line contains an integer, , denoting the size of the array.
The second line contains  space-separated integers describing an array of numbers .
Constraints
0<n<=100
-100<=arr[i][j]<=100
Output Format
You must print the following  lines:
A decimal representing of the fraction of positive numbers in the array compared to its size.
A decimal representing of the fraction of negative numbers in the array compared to its size.
A decimal representing of the fraction of zeros in the array compared to its size.
Sample Input
6
-4 3 -9 0 4 1
Sample Output
0.500000
0.333333
0.166667
'''


def plus_minus(arr):
    n = len(arr)

    plus = len([x for x in arr if x>0])/n
    minus = len([x for x in arr if x<0])/n
    zeros = len([x for x in arr if x==0])/n

    print(format(plus, ".6f"))
    print(format(minus,".6f"))
    print(format(zeros,".6f"))


n = int(input())
arr = list(map(int, input().rstrip().split()))
plus_minus(arr)