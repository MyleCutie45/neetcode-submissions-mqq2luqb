class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        st = {}
        ts = {}
        for a , b in zip(s,t):
            if a in st:
                if st[a] != b:
                    return False
            else:
                st[a]=b 
            if b in ts:
                if ts[b] != a:
                    return False
            else: ts[b] = a 
        return True