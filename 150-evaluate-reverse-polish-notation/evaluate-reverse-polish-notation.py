from collections import deque
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = deque()
        for ch in tokens:
            if ch == '+':
                n1 = int(st.pop())
                n2 = int(st.pop())
                st.append(n2 + n1)
            elif ch == '-':
                n1 = int(st.pop())
                n2 = int(st.pop())
                st.append(n2 - n1)
            elif ch == '*':
                n1 = int(st.pop())
                n2 = int(st.pop())
                st.append(n2 * n1)
            elif ch == '/':
                n1 = int(st.pop())  
                n2 = int(st.pop())
                st.append(int(n2 / n1))
            else: st.append(int(ch))
        return st[-1]