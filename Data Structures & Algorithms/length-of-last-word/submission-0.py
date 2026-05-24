class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        res = s.strip().split()
        n = len(res) 
        return len(res[n-1])