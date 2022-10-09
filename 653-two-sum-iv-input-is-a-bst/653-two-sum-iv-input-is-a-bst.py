# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        
        def inorder(root, traversal):
            if root is None:
                return
            inorder(root.left, traversal)
            traversal.append(root.val)
            inorder(root.right, traversal)
            
        traversal = []
        inorder(root, traversal)
        left = 0
        right = len(traversal)-1
        while left<right:
            if traversal[left]+traversal[right]==k:
                return True
            if traversal[left]+traversal[right]<k:
                left+=1
            else:
                right-=1
        return False