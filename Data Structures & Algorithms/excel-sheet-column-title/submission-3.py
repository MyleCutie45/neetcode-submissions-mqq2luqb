class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        n = columnNumber
        res = []
        while n > 0:
            n-=1
            res.append(chr(ord('A')+(n%26)))
            n//=26
        return "".join(reversed(res))
