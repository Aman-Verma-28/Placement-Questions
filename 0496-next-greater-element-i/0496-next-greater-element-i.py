class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        len_ = len(nums2)
        mapping = dict()
        for index in range(len_-1,-1,-1):
            if len(stack)==0:
                mapping[nums2[index]]=-1
                stack.append(nums2[index])
            else:
                while len(stack)>0 and stack[-1]<nums2[index]:
                    stack.pop()
                if len(stack)==0:
                    mapping[nums2[index]]=-1
                else:
                    mapping[nums2[index]]=stack[-1]
                stack.append(nums2[index])
        ans = []
        for val in nums1:
            ans.append(mapping[val])
        return ans
        