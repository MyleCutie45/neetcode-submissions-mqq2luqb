class Solution:
    def isHappy(self, n: int) -> bool:
        visit = set()
        while n not in visit:
            visit.add(n)
            n = self.sumOf2(n)
            if n==1: return True
        return False 

    def sumOf2(self,n):
        res=0
        while n:
            d = n % 10
            d = d**2
            res += d 
            n = n//10
        return res