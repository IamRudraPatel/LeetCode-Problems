class Solution:
    def removeSubString(self, st, subSt):
        stack = []
        for ch in st:
            if (stack) and ((stack[-1]+ch) == subSt):
                stack.pop()
            else:
                stack.append(ch)
        return "".join(stack)
    def maximumGain(self, s: str, x: int, y: int) -> int:
        n = len(s)
        maxi, mini = -1, -1
        maxStr, minStr = "", ""
        if x > y:
            maxStr, minStr = "ab", "ba"
            maxi, mini  = x, y
        else: 
            maxStr, minStr = "ba", "ab"
            maxi, mini = y, x
        score = 0
        tempSt = self.removeSubString(s, maxStr)
        L = len(tempSt)
        score += ((n - L) // 2) * maxi
        tempSt = self.removeSubString(tempSt, minStr)
        newL = len(tempSt)
        score += ((L - newL) // 2) * mini
        return score
