class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        length = len(nums)
        ind = 0
        while ind<length:
            val = nums[ind]
            while nums[ind] != nums[val-1]:
                nums[ind], nums[val-1] = nums[val-1], nums[ind]
                val = nums[ind]
            ind += 1
        for ind in range(length):
            if nums[ind]!=ind+1:
                repeating = nums[ind]
                missing = ind+1
                return [repeating, missing]
        
        