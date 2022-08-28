def subarraysum(nums, k):
	ans=0
	s=set()
	cur=0
	for i in nums:
		cur+=i
		if cur==k or cur-k in s:
			ans+=1
		if cur not in s:
			s.add(cur)
	if cur==k or cur-k in s:
		ans+=1
	return ans

print(subarraysum(input(), input()))