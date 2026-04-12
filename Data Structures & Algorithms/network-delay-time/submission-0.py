class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = [[] for _ in range(n+1)]
        for u,v,w in times:
            adj[u].append((v,w))
        #Min heap (distance, node)
        pq = [(0,k)]
        dist = [float('inf')]*(n+1)
        dist[k]=0
        while pq:
            d,u=heapq.heappop(pq)
            if d > dist[u]:
                continue
            for v,w in adj[u]:
                if dist[u]+w<dist[v]:
                    dist[v]=dist[u]+w
                    heapq.heappush(pq,(dist[v],v))
        max_time= max(dist[1:])
        return max_time if max_time != float('inf') else -1
