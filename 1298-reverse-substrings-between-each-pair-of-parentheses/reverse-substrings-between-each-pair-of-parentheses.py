class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        bracketsMap = {}
        n = len(s)
        for i in range(n):
            if s[i] == '(': stack.append(i)
            elif s[i] == ')':
                idx = stack.pop()
                bracketsMap[idx] = i
                bracketsMap[i] = idx
        ans = ""
        direct = 1
        i = 0
        while (i<n):
            if (s[i] == '(') or (s[i] == ')'):
                i = bracketsMap[i]
                direct *= -1
            else: ans += s[i]
            i += direct
        return ans
