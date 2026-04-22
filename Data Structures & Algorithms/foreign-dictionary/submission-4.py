from collections import defaultdict, deque


class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = defaultdict(set)
        indegree = {}
        for word in words:
            for c in word:
                indegree[c] = 0
        for i in range(len(words)-1):
            w1,w2 = words[i],words[i+1]
            if len(w1) > len(w2) and w1.startswith(w2):
                return ""
            for c1,c2 in zip(w1,w2):
                if c1 != c2:
                    if c2 not in adj[c1]:
                        adj[c1].add(c2)
                        indegree[c2]+=1
                    break 
        q = deque([c for c in indegree if indegree[c] == 0])
        res = []
        while q:
            u = q.popleft()
            res.append(u)
            for v in adj[u]:
                indegree[v]-=1
                if indegree[v]==0:
                    q.append(v)
        if len(res) != len(indegree):
            return ""
        return "".join(res)


        
