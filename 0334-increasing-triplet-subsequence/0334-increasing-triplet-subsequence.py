class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums)<3:
            return False
        mini = sys.maxsize
        mid = sys.maxsize
        for num in nums:
            if num<=mini:
                mini=num
            elif num<=mid:
                mid=num
            else:
                return True
        return False