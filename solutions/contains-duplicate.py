from collections import Counter


def containsDuplicate(nums):
    numCounter = Counter(nums)

    for k in numCounter:
        if numCounter[k] > 1:
            return True

    return False
