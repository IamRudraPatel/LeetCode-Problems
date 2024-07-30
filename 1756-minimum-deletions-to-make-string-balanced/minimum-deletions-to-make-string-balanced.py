class Solution:
    def minimumDeletions(self, s: str) -> int:
        ans, bCount = 0, 0
        for ch in s:
            if ch == 'b': bCount += 1
            elif bCount:
                ans += 1
                bCount -= 1
        return ans