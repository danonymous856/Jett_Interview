def maxProfit(prices: list[int]) -> int:
    l, r = 0, 1 #1)left = buy, 2)right = sell
    maxp = 0

    while r<len(prices):
        if prices[l] < prices[r]:
            profit = prices[r] - prices[l]
            maxp = max(maxp,profit)
        else:
            l = r
        r+=1

    return maxp

print(maxProfit([7,1,5,3,6,4]))