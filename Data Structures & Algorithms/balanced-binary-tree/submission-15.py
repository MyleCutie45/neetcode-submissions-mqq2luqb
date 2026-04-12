class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def dfs(self,node):
            if not node:
                return 0
            left = dfs(self,node.left) 
            right = dfs(self,node.right)
            if(left==-1):
                return -1
            if(right==-1):
                return -1
            if(abs(left-right)>1):
                return -1
            return 1 + max(left,right)

        return dfs(self,root) != -1