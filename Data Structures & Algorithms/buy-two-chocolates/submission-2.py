class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        shaco = sorted(prices)
        for i in range(len(prices)-1):
            ok = shaco[i] + shaco[i+1]
            if ok <= money:
                return (money - ok) if  (money - ok) >= 0 else money  
        return money
        