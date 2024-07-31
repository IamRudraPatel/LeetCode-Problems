class Solution:
    def countKeyChanges(self, s: str) -> int:
        lc = s[0].lower()
        ans = 0
        for i in range(1, len(s)):
            ch = s[i].lower()
            if ch != lc:
                ans += 1
            lc = ch
        return ans
