'''
Given a square matrix, calculate the absolute difference between the sums of its diagonals.
For example, the square matrix  is shown below:
1 2 3
4 5 6
9 8 9
The left-to-right diagonal = . The right to left diagonal = . Their absolute difference is .
Function description
Complete the  function in the editor below. It must return an integer representing the absolute diagonal difference.
diagonalDifference takes the following parameter:
arr: an array of integers .
Input Format
The first line contains a single integer, , the number of rows and columns in the matrix .
Each of the next  lines describes a row, , and consists of  space-separated integers .
Constraints
-100<=arr[i][j]<=100
Output Format
Print the absolute difference between the sums of the matrix's two diagonals as a single integer.
Sample Input
3
11 2 4
4 5 6
10 8 -12
Sample Output
15
'''

def diagonalDifference(arr):
    sum1 = sum2 = 0
    num_rows = num_cols = len(arr)

    for i in range(num_rows):
        for j in range(num_cols):
            if i==j:
                sum1 += arr[i][i]
            if i+j==num_rows-1:
                sum2 += arr[i][j]

    return abs(sum1-sum2)


n = int(input().strip())
arr = []

for _ in range(n):
    arr.append(list(map(int, input().rstrip().split())))

result = diagonalDifference(arr)
print(result)