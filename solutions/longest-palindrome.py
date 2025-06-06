from collections import Counter


def longestPalindrome(s):
    c = Counter(s)

    total = 0
    hasOdd = 0
    for k, v in c.items():
        if v % 2 == 0:
            total += v
        else:
            hasOdd = 1
            total += v - 1

    return total + hasOdd
