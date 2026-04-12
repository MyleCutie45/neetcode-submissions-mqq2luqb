class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if(sum(gas)<sum(cost)):
            return -1
        jungle_diff = [0] * len(gas) 
        for i in range(0,len(gas)):
            jungle_diff[i] = gas[i] - cost[i]
        res = 0
        total = 0
        for i in range(0,len(jungle_diff)):
            total += jungle_diff[i]
            if total < 0:
                total = 0
                res = i + 1
        return res