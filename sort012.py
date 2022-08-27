def sortedColors(nums):
	low = 0
	n = len(nums)
	high = n-1
	mid = 0
	while mid<=high:
		if nums[mid] == 0:
			nums[mid], nums[low] = nums[low], nums[mid]
			mid+=1
			low+=1
		elif nums[mid] == 1:
			mid+=1
		else:
			nums[mid], nums[high] = nums[high], nums[mid]
			high-=1


nums = list(input())
# nums = list(map(int,input().split()))
sortedColors(nums)
print(nums)

