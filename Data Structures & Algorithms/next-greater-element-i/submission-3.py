class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        for x in nums1:
            idx = nums2.index(x)
            ans = -1

            for j in range(idx + 1, len(nums2)):
                if nums2[j] > x:
                    ans = nums2[j]
                    break

            res.append(ans)

        return res