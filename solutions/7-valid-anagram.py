from collections import Counter


def isAnagram(s, t):
    sCounter = Counter(s)
    tCounter = Counter(t)

    return sCounter == tCounter
