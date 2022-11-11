class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        ans=0
        i=0
        n=len(nums)
        while i<n:
            j=nums[i]
            while i<n and nums[i]==j:
                i+=1
            nums[ans]=j
            ans+=1
        return ans
            
            
                