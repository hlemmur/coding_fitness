'''
Task
Complete the code in the editor below. The variables i, d, and s are already declared and initialized for you. You must:
Declare 3 variables: one of type int, one of type double, and one of type String.
Read 3 lines of input from stdin (according to the sequence given in the Input Format section below) and initialize your 3 variables.
Use the  operator to perform the following operations:
Print the sum of i plus your int variable on a new line.
Print the sum of d plus your double variable to a scale of one decimal place on a new line.
Concatenate s with the string you read as input and print the result on a new line.
'''


i = 4
d = 4.0
s = 'HackerRank '

# Declare second integer, double, and String variables.
i2 = 0
d2 = 0.0
s2 = ''

# Read and save an integer, double, and String to your variables.
i2 = int(input())
d2 = float(input())
s2 = input()

# Print the sum of both integer variables on a new line.
print(i+i2)
# Print the sum of the double variables on a new line.
print(d+d2)
# Concatenate and print the String variables on a new line
# The 's' variable above should be printed first.
print(s+s2)