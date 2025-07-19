from collections import Counter


def findAnagrams(s, p):
    pLen = len(p)
    pCounter = Counter(p)

    finalIndexes = []

    for i in range(len(s) - pLen + 1):
        if Counter(s[i : i + pLen]) == pCounter:
            finalIndexes.append(i)

    return finalIndexes
