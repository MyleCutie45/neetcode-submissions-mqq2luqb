class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        for u,v,w in flights:
            graph[u].append((v,w))
        q = deque([(src,0,0)])
        dist = [float('inf')]*n
        dist[src]=0
        while q:
            node,cost,stops=q.popleft()
            if stops>k:
                continue
            for nei,w in graph[node]:
                new_cost=cost+w 
                if new_cost < dist[nei]:
                    dist[nei]=new_cost 
                    q.append((nei,new_cost,stops+1))
        return -1 if dist[dst] == float('inf') else dist[dst]