class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        length = len(nums)
        ind = 0
        
        while ind<length:
            if nums[ind]<=0 or nums[ind]>length:
                ind+=1
            else:
                val = nums[ind]
                while nums[ind]!=nums[val-1]:
                    nums[val-1], nums[ind] = nums[ind], nums[val-1]
                    val = nums[ind]
                    if val<=0 or val>length:
                        break
                ind+=1
        
        for index in range(length):
            if nums[index]!=index+1:
                return index+1
        return length+1