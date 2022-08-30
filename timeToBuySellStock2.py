def stockBuySell(price, n):
	ans = []
	buy = 0
	for i in range(1,n):
		if price[i]<price[i-1]:
			if i-1!=buy:
				ans.append((buy, i-1))
			buy = i
	if i!=buy:
		ans.append((buy, i))

	return ans

print(stockBuySell(price=[23, 13, 25, 29, 33, 19, 34, 45, 65, 67], n=10))
