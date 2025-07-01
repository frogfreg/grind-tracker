def productExceptSelf(nums):
    pre = [0] * len(nums)
    post = [0] * len(nums)

    for i in range(len(nums)):
        if i == 0:
            pre[i] = 1
            continue

        pre[i] = pre[i - 1] * nums[i - 1]

    for i in range(len(nums) - 1, -1, -1):
        if i == (len(nums) - 1):
            post[i] = 1
            continue

        post[i] = post[i + 1] * nums[i + 1]

    final = [0] * len(nums)

    for i in range(len(nums)):
        final[i] = pre[i] * post[i]

    return final
