class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        lol = set(nums)
        if len(lol) == len(nums): return False
        return True