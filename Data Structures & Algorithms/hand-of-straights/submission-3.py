class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        mapo = {}
        for i in hand:
            mapo[i] = 1 + mapo.get(i,0)
        petty = list(mapo.keys())
        heapq.heapify(petty)
        while petty:
            first = petty[0]
            for i in range(first,first+groupSize):
                if i not in mapo:
                    return False
                mapo[i]-=1
                if mapo[i] == 0:
                    if petty[0] != i: # t dang can i co 
                        return False
                    heapq.heappop(petty)
        return True
