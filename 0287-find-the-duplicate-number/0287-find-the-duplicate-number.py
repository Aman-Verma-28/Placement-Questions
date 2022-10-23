class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        ind = 0
        n = len(nums)
        while ind < n:
            while nums[nums[ind] - 1] != nums[ind]:
                print(nums[nums[ind] - 1], nums[ind])
                temp = nums[ind]-1
                temp2 = nums[temp]
                nums[temp] = nums[ind]
                nums[ind] = temp2
                # nums[ind], nums[nums[ind] - 1] = nums[nums[ind] - 1], nums[ind]
            ind += 1
        return nums[-1]

            