def majorityElement(nums):
	ele = nums[0]
	cur = 1
	for i in nums[1:]:
		if cur==0:
			ele = i
			cur = 1
		else:
			if ele == i:
				cur+=1
			else:
				cur-=1
	return ele


print(majorityElement(nums = [2,2,1,1,1,2,2]))
print(majorityElement(nums = [3,2,3]))