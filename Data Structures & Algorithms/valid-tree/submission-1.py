# A graph is a valid tree if:
# It has no cycles
# It is fully connected
# If the graph has more than n−1 edges, it must contain a cycle, so it cannot be a tree.
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > n - 1 : return False
        adj = [[] for _ in range(n)]
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        visit = set()
        def dfs(i,p):
            visit.add(i)
            for nugga in adj[i]:
                if nugga not in visit:
                    if dfs(nugga,i):
                        return True
                elif (nugga != p):
                    return True
            return False
        return not dfs(0,-1) and len(visit) == n
