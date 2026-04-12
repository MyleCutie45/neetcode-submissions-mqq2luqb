class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        #min(distance from i to ANY node already in MST)
        minDist  = [float('inf')] * n
        visited = [False] * n
        minDist[0]=0
        result=0
        for _ in range(n):
            ## 1. pick smallest node
            u=-1
            for i in range(n):
                #we haven’t picked any node yet (u == -1)
                #OR we found a better (cheaper) node
                if not visited[i] and (u==-1 or minDist[i]<minDist[u]):
                    u = i 
            visited[u] = True
            result += minDist[u]
            for v in range(n):
                if not visited[v]:
                    dist = abs(points[u][0] - points[v][0]) + abs(points[u][1] - points[v][1])
                    minDist[v] = min(minDist[v],dist)
        return result