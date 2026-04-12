from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def dfs(dih: List[int]) -> int:
            if len(dih) == 1:
                return dih[0]
            dp = [0] * len(dih)
            dp[0] = dih[0]
            dp[1] = max(dp[0], dih[1])

            for i in range(2, len(dih)):
                dp[i] = max(dp[i-1], dih[i] + dp[i-2])

            return dp[-1]

        return max(dfs(nums[1:]), dfs(nums[:-1]))