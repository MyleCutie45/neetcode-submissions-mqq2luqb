class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        res = ()
        mapo = {}
        for i, n in enumerate(numbers):
            diff = target - n
            if diff in mapo:
                return[mapo[diff]+1,i+1]
            mapo[n] = i