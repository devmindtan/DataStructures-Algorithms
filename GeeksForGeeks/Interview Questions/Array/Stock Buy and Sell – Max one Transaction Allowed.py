def maximumProfit(prices):
    minSoFar = prices[0]
    res = 0

    for i in range(1, len(prices)):
        minSoFar = min(minSoFar, prices[i])

        res = max(res, prices[i] - minSoFar)

    return res


if __name__ == "__main__":
    prices = [7, 10, 2, 3, 6, 9, 1]
    # prices = [7, 6, 4, 3, 1]
    # prices = [1, 3, 6, 9, 11]
    print(maximumProfit(prices))
