def climbStairs(n, dp):
	if n==0:
		dp[0]=1
		return 1
	if n==1:
		dp[n] = n
		return n
	if dp[n]==-1:
		dp[n] = climbStairs(n-1, dp) + climbStairs(n-2, dp)		
	return dp[n]

t = int(input())
for _ in range(t):
	n = int(input())
	dp = [-1]*(n+1)
	print(climbStairs(n, dp))