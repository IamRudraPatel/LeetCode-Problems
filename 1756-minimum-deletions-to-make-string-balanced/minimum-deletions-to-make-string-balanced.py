from collections import deque
class Solution:
    def minimumDeletions(self, s: str) -> int:
        st1 = deque()
        ans1: int = 0
        for ch in s:
            if (ch == 'a') and (st1) and (st1[-1]=='b'):
                ans1 += 1
                st1.pop()
            else:st1.append(ch)
        return ans1