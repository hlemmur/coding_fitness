'''
Consider a staircase of size :
   #
  ##
 ###
####
Observe that its base and height are both equal to , and the image is drawn using # symbols and spaces. The last line is not preceded by any spaces.
Write a program that prints a staircase of size .
Function Description
Complete the staircase function in the editor below. It should print a staircase as described above.
staircase has the following parameter(s):
n: an integer
Input Format
A single integer, , denoting the size of the staircase.
Constraints
0<n<=100
Output Format
Print a staircase of size  using # symbols and spaces.
Note: The last line must have  spaces in it.
Sample Input
6
Sample Output
     #
    ##
   ###
  ####
 #####
######
'''


def staircase(n):
    for i in range(n):
        str = ''
        for j in range(n):
            if i >= n-j-1:
                str += '#'
            else:
                str+=' '
        print (str)


n = int(input())
staircase(n)

