# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        
        queue = deque()
        count = 0
        if root is None:
            return 0
        
        count += 1
        queue.append(root)
        
        while len(queue) > 0:
            root = queue.popleft()
            
            if root.left:
                count += 1
                queue.append(root.left)
            
            else:
                break
                
            if root.right:
                count += 1
                queue.append(root.right)
            
            else:
                break
                
        return count
        