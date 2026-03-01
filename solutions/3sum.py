def threeSum(nums: list[int]) -> list[list[int]]:
    triplets = set()
    seen = set()

    for i, target in enumerate(nums):
        if target in seen:
            continue

        seen.add(target)
        pairs = twoSum(-target, nums, i)

        for p in pairs:
            triplets.add(tuple(sorted([target, p[0], p[1]])))

    return list(triplets)


def twoSum(target, nums, x) -> list:
    seen = set()
    pairs = []

    for i, n in enumerate(nums):
        if i == x:
            continue

        if (target - n) in seen:
            pairs.append([n, target - n])
        else:
            seen.add(n)

    return pairs
