from collections import Counter

class Solution:
    def maxDifference(self, s: str) -> int:
        freq = Counter(s)

        max_odd = max(cnt for cnt in freq.values() if cnt % 2 == 1)
        min_even = min(cnt for cnt in freq.values() if cnt % 2 == 0)

        return max_odd - min_even