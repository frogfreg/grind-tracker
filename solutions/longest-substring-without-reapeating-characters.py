def lengthOfLongestSubstring(s):
    best = 0
    seenAt = {}
    left = 0

    for i, letter in enumerate(s):
        if letter not in seenAt or seenAt[letter] < left:
            best = max(best, i - left + 1)
            seenAt[letter] = i
        else:
            left = seenAt[letter] + 1
            seenAt[letter] = i

    return best
