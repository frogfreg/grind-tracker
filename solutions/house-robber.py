from functools import cache


def rob(nums: list[int]) -> int:
    @cache
    def maxRobEndingAt(i):
        if i < 0:
            return 0

        prev2 = i - 2
        prev3 = i - 3

        return nums[i] + max(maxRobEndingAt(prev2), maxRobEndingAt(prev3))

    currMax = 0
    for i in range(len(nums) - 1, -1, -1):
        currMax = max(currMax, maxRobEndingAt(i))

    return currMax
