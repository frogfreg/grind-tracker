import math


def maxSubArray(nums):
    maxSum = -(math.inf)
    currSum = 0

    for n in nums:
        currSum = max(currSum + n, n)
        maxSum = max(maxSum, currSum)

    return maxSum
