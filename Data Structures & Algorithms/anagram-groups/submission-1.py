class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapo = {}
        for s in strs:
            sortah = ''.join(sorted(s))
            if sortah not in mapo:
                mapo[sortah] = []
            mapo[sortah].append(s)
        return list(mapo.values())