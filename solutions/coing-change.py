import math


def coinChange(coins, amount):
    cache = {}
    res = minCoins(cache, coins, amount)

    if math.isinf(res):
        return -1

    return res


def minCoins(cache, coins, amount):
    if amount < 0:
        return math.inf
    if amount == 0:
        return 0
    if amount in cache:
        return cache[amount]

    res = 1 + min([minCoins(cache, coins, amount - c) for c in coins])
    cache[amount] = res

    return res
