def uniquePathsFunc(m: int, n: int) -> int:
    cache = {}

    tup = (0, 0)

    return pathCount(m, n, cache, tup)


def pathCount(m: int, n: int, cache: dict, tup: tuple) -> int:
    if tup == (m - 1, n - 2) or tup == (m - 2, n - 1) or tup == (m - 1, n - 1):
        return 1

    if tup[0] >= m or tup[1] >= n:
        return 0

    if tup in cache:
        return cache[tup]

    down = (tup[0] + 1, tup[1])
    right = (tup[0], tup[1] + 1)

    totalPaths = pathCount(m, n, cache, down) + pathCount(m, n, cache, right)
    cache[tup] = totalPaths

    return totalPaths
