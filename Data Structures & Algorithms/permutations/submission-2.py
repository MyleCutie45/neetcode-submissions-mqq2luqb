class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(perm,nums,pick):
            if len(perm) == len(nums):
                res.append(perm.copy())
                return
            for i in range(0,len(nums)):
                if not pick[i]:
                    pick[i] = True            
                    perm.append(nums[i])
                    dfs(perm,nums,pick)
                    perm.pop()
                    pick[i]  = False
        dfs([],nums,[False]*len(nums))
        return res