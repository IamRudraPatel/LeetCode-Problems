class Solution:
    def isBracket(self, ch) -> bool:
        if ch=='(' or ch==')': return True
        return False
    
    def reverseRange(self, st, low, high) -> None:
        while (low <= high):
            if (not self.isBracket(st[low])) and (not self.isBracket(st[high])):
                st[low], st[high] = st[high], st[low]
                low += 1
                high -= 1
                continue
            if self.isBracket(st[low]):
                low += 1
            if self.isBracket(st[high]):
                high -= 1

    def reverseParentheses(self, s: str) -> str:
        st = list(s)
        stack = []
        for i in range(len(st)):
            if st[i]=='(':
                stack.append(i)
            elif st[i]==')':
                self.reverseRange(st, stack.pop()+1, i-1)
            else: continue
        ans = ""
        for ch in st:
            if not self.isBracket(ch):
                ans += ch
        return ans