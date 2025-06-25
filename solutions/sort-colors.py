def sortColors(nums):
    """
    Do not return anything, modify nums in-place instead.
    """
    rCount = 0
    wCount = 0
    bCount = 0

    for n in nums:
        if n == 0:
            rCount += 1
        elif n == 1:
            wCount += 1
        else:
            bCount += 1

    for i in range(len(nums)):
        if i < rCount:
            nums[i] = 0
        elif rCount <= i < (rCount + wCount):
            nums[i] = 1
        else:
            nums[i] = 2
