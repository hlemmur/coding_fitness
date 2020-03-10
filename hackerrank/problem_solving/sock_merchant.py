'''
John works at a clothing store. He has a large pile of socks that he must pair by color for sale. Given an array of integers representing the color of each sock, determine how many pairs of socks with matching colors there are.
For example, there are  socks with colors . There is one pair of color  and one of color . There are three odd socks left, one of each color. The number of pairs is .
Function Description
Complete the sockMerchant function in the editor below. It must return an integer representing the number of matching pairs of socks that are available.
sockMerchant has the following parameter(s):
n: the number of socks in the pile
ar: the colors of each sock

Input Format
The first line contains an integer , the number of socks represented in .
The second line contains  space-separated integers describing the colors  of the socks in the pile.

Constraints
1<=n<=100
1<=ar[i]<=100 where 0<=i<n

Output Format
Return the total number of matching pairs of socks that John can sell.
Sample Input
9
10 20 20 10 10 30 50 10 20
Sample Output
3'' \
'''

def sockMerchant(n, ar):
    do = True
    while do:
        do = False
        for i in range(n-1):
            if ar[i+1] < ar[i]:
                ar[i], ar[i+1] = ar[i+1], ar[i]
                do = True

    countTotalPairs = 0

    start = 0
    while start < n:
        count_one_color = 1
        for j in range(start+1, n):
            if ar[j] == ar[start]:
                count_one_color += 1
            elif ar[j] > ar [start]:
                start = j
                break
            if j == n-1:
                start = n
                break
        countTotalPairs += count_one_color//2

    return countTotalPairs


n = 9
ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]

#n = 10
#ar = [1, 1, 3, 1, 2, 1, 3, 3, 3, 3]
print(sockMerchant(n, ar))