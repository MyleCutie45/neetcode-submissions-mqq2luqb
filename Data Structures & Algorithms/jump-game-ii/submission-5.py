class Solution:
    def jump(self, nums: List[int]) -> int:
        l,r = 0,0
        dih = 0
        res = 0
        while r < len(nums) - 1:
            dih = 0
            for i in range(l,r+1):
                dih = max(dih,nums[i]+i)
            l = r + 1
            r = dih
            res += 1
        return res