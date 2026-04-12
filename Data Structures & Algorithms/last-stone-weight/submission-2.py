class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)
        while(len(stones)>1):
            x1 = heapq.heappop(stones)
            x2 = heapq.heappop(stones)
            if(x2>x1):
                heapq.heappush(stones,-(x2-x1))
        stones.append(0)
        return abs(stones[0])
        