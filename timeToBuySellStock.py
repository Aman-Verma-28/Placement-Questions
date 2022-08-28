def maxProfit(prices):
	ans = 0
	buy = prices[0]
	n = len(prices)
	for i in range(1,n):
		buy = min(buy, prices[i])
		ans = max(ans, prices[i]-buy)
	return ans
print(maxProfit(input()))