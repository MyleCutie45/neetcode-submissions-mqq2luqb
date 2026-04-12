# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = -float('inf')
        def dfs(root):
            nonlocal res
            if not root:
                return 0
            left = max(0,dfs(root.left))
            right = max(0,dfs(root.right))
            res = max(res,root.val + left + right) #cannot be extended upward
            return root.val + max(left,right) # Return upward
        dfs(root)
        return res