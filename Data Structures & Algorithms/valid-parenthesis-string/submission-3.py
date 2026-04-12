class Solution:
    def checkValidString(self, s: str) -> bool:
        n = len(s)
        leftMax=0
        leftMin=0
        for c in s:
            if c=='(':
                leftMax+=1
                leftMin+=1
            elif c==')':
                leftMax-=1
                leftMin-=1
            elif c=='*':
                leftMax+=1
                leftMin-=1
            if leftMin < 0:
                leftMin=0
            if leftMax < 0:
                return False
        return leftMin==0
            