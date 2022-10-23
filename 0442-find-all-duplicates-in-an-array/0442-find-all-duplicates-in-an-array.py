class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = set()
        length = len(nums)
        ind = 0
        while ind<length:
            val = nums[ind]
            while nums[val-1]!=nums[ind]:
                nums[val-1], nums[ind] = nums[ind], nums[val-1]
                val = nums[ind]
            if nums[val-1] == nums[ind] and ind!=val-1:
                ans.add(nums[ind])
            ind += 1
        return ans