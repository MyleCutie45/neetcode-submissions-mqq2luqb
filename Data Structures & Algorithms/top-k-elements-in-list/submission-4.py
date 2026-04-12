class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mapo = {}
        for nb in nums:
            mapo[nb] = 1 + mapo.get(nb,0)
        ayaya = [(key,value) for key , value in mapo.items()]
        nigiyaka = sorted(ayaya , key=lambda x : (x[1],x[0]) , reverse = True)
        res = []
        for i in range(0,k):
            res.append(nigiyaka[i][0])
        return res
