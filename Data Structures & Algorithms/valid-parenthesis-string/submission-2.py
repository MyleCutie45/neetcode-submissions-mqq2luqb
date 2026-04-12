# low → minimum possible number of open '('
# high → maximum possible number of open '('

class Solution:
    def checkValidString(self, s: str) -> bool:
        lower = 0
        upper = 0
        n = len(s)
        for i in range(n):
            if s[i] == '(':
                lower+=1
                upper+=1
            elif s[i] == ')':
                lower-=1
                upper-=1
            elif s[i] == '*':
                lower-=1
                upper+=1
            if lower < 0:
                lower = 0
            if upper < 0:
                return False
        return lower == 0
            