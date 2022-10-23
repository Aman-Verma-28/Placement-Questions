class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        ind = 0
        n = len(nums)
        while ind < n:
            val = nums[ind]
            while nums[val-1]!=nums[ind]:
                nums[val-1], nums[ind] = nums[ind], nums[val-1]
                val = nums[ind]
            
                
            ind += 1
        return nums[-1]

            