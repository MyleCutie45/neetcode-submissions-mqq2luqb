class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        count_1 = 0
        for i in range(len(s)):
            if s[i] == '1':
                count_1+=1
        count_0 = len(s) - count_1
        res =''
        for i in range(count_1-1):
            res += '1'
        for i in range(count_0):
            res += '0'
        res += '1'
        return res