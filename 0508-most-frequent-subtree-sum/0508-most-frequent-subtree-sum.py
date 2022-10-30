# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        
        def helper(root, frequency):
            if root is None:
                return 0
            
            left = helper(root.left, frequency)
            right = helper(root.right, frequency)
            
            currentSum = left+right+root.val
            
            if currentSum in frequency:
                frequency[currentSum] += 1
            else:
                frequency[currentSum] = 1
            
            return currentSum
        
        frequency = {}
        helper(root, frequency)
        
        maxFrequency = max(frequency.values())
        
        ans = []
        
        for key, val in frequency.items():
            if val == maxFrequency:
                ans.append(key)
        
        return ans
            