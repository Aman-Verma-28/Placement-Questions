class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        
        # Subarray sum = k
        
        prevSum = {0:-1}
        curSum = 0
        for ind,val in enumerate(nums):
            curSum+=(val%k)
            curSum%=k
            if curSum in prevSum:
                if ind-prevSum[curSum]>=2:
                    return True
            else:
                prevSum[curSum] = ind
        return False                