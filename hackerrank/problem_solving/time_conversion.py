'''
Given a time in -hour AM/PM format, convert it to military (24-hour) time.
Note: Midnight is 12:00:00AM on a 12-hour clock, and 00:00:00 on a 24-hour clock. Noon is 12:00:00PM on a 12-hour clock, and 12:00:00 on a 24-hour clock.
Function Description
Complete the timeConversion function in the editor below. It should return a new string representing the input time in 24 hour format.
timeConversion has the following parameter(s):
s: a string representing time in 12 hour format
Input Format
A single string  containing a time in 12-hour clock format (i.e.: hh:mm:ssAM or hh:mm:ssPM), where 01<=hh<=12 and 00<=mm,ss<=59.
Constraints
All input times are valid
Output Format
Convert and print the given time in 24-hour format, where 00<=hh<=23.
Sample Input 0
07:05:45PM
Sample Output 0
19:05:45
'''


def timeConversion(s):
    length = len(s)
    part = s[length-2: length]
    hours = int(s[0:2])
    s_new = s[:length-2]

    if part == 'PM' and hours!=12:
        s_new = str(hours+12) + s[2:length-2]
    elif part == 'AM' and hours==12:
        s_new = '00' + s[2:length-2]

    return s_new


s = input()
result = timeConversion(s)
print(result)