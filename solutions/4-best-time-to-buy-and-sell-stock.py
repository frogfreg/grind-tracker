def maxProfit(prices):
    currBest = 0
    bestBuy = prices[0]

    for p in prices[1:]:
        currBest = max(currBest, p - bestBuy)
        bestBuy = min(bestBuy, p)

    return currBest
