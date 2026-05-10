class Solution:
    def maxDepth(self, s: str) -> int:
        count = 0
        res =0
        for i in range(len(s)):
            if s[i] == '(':
                count += 1
                res = max(res,count)
            elif s[i]==')' : 
                count -=1
        return res