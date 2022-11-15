# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        
        def helper(root, count):
            if root is None:
                return
            
            left = 1
            temp = root
            while temp.left is not None:
                temp = temp.left
                left += 1
            
            
            right = 1
            temp=root
            while temp.right is not None:
                temp = temp.right
                right += 1
            
        
            
            if left == right:
                print('inside if', root.val, left, right)
                count[0] += pow(2, left) - 1
                
            else:
                print(root.val, left, right)
                count[0] += 1
                helper(root.left, count)
                helper(root.right, count)
                
            
        count = [0]
        helper(root, count)
        
        return count[0]
            
        