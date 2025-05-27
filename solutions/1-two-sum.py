def twoSum(nums, target):
    seenAtIndex = {}

    for i, n in enumerate(nums):
        if target - n in seenAtIndex:
            return [i, seenAtIndex[target - n]]

        seenAtIndex[n] = i
