"""
We consider two strings to be anagrams of each other if the first string's letters can be rearranged to form the second string. In other words, both strings must contain the same exact letters in the same exact frequency. For example, bacdc and dcbac are anagrams, but bacdc and dcbad are not.

Alice is taking a cryptography class and finding anagrams to be very useful. She decides on an encryption scheme involving two large strings where encryption is dependent on the minimum number of character deletions required to make the two strings anagrams. Can you help her find this number?

Given two strings,  s1 and s2, that may not be of the same length, determine the minimum number of character deletions required to make s1 and s2  anagrams. Any characters can be deleted from either of the strings.

For example, s1=abc and s2=amnop. The only characters that match are the a's so we have to remove ab from s1 and mnop from s2 for a total 6 of  deletions.

Function Description

Complete the makingAnagrams function in the editor below. It should return an integer representing the minimum number of deletions needed to make the strings anagrams.

makingAnagrams has the following parameter(s):
s1: a string
s2: a string

It is guaranteed that s1 and 2 consist of lowercase English letters, ascii[a-z].
"""

import math
import os
import random
import re
import sys
import string

# Complete the makingAnagrams function below.
def makingAnagrams(s1, s2):
    str1 = "".join(sorted(list(s1)))
    str2 = "".join(sorted(list(s2)))

    counter = 0

    dict1 = dict.fromkeys(string.ascii_lowercase, 0)
    dict2 = dict1.copy()

    for c in str1:
        dict1[c] += 1

    for c in str2:
        dict2[c] += 1


    counter = sum([abs(v1 - v2) for (v1, v2) in zip(dict1.values(), dict2.values())])

    return counter

if __name__ == '__main__':

    s1 = 'ahoadpe'

    s2 = 'pwad'

    result = makingAnagrams(s1, s2)

    print(result)