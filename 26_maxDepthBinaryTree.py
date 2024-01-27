from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None: return 0
        l = self.maxDepth(root.left)
        r = self.maxDepth(root.right)
        return 1+max(l,r)

# [3,9,20,null,null,15,7]
root = TreeNode(3)
root.left = TreeNode(9)
l = TreeNode(20)
l.right = TreeNode(15)
l.left = TreeNode(7)
root.right = l
print(Solution().maxDepth(root))