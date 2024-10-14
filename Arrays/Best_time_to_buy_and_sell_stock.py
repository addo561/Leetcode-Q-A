link = 'https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/'

def maxprofit(prices):
    buy = prices[0]
    profit = 0
    for p in prices[1:]:
        if buy>p:
            buy = p
        profit= max(profit,p-buy)
    return profit                   