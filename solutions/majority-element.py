from collections import Counter


def majorityElement(nums):
    c = Counter(nums)

    return c.most_common(1)[0][0]
