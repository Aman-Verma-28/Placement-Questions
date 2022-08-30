def maxSubarray(nums):
	curSum = 0
	maxSum = 0
	initialPointer = 0
	nextPointer = 0
	for i,num in enumerate(nums):
		curSum+=num
		if curSum>maxSum:
			maxSum = curSum
			nextPointer = i
		if curSum<0:
			curSum = 0
			initialPointer = i
	return maxSum

print(maxSubarray( nums = [-2,1,-3,4,-1,2,1,-5,4]))
print(maxSubarray( nums = [5,4,1,7,8]))
print(maxSubarray( nums = [1]))
print(maxSubarray(nums = [-2, -3]))