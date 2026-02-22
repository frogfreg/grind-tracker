def search(self, nums: list[int], target: int) -> int:
    indexOfTiniest = nums.index(min(nums))
    move = len(nums) - indexOfTiniest

    sorNums = sorted(nums)

    lower = 0
    upper = len(sorNums) - 1

    while lower <= upper:
        currIdx = (lower + upper) // 2

        if sorNums[currIdx] == target:
            newIdx = currIdx - move
            if newIdx < 0:
                newIdx += len(sorNums)

            return newIdx

        if sorNums[currIdx] > target:
            upper = currIdx - 1
        else:
            lower = currIdx + 1

    return -1
