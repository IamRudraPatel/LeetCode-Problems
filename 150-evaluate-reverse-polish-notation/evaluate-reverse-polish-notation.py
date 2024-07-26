from collections import deque
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = deque()
        for ch in tokens:
            if ch == '+':
                st.append(st.pop() + st.pop())
            elif ch == '-':
                n1, n2 = st.pop(), st.pop()
                st.append(n2 - n1)
            elif ch == '*':
                st.append(st.pop() * st.pop())
            elif ch == '/':
                n1, n2 = st.pop(), st.pop()
                st.append(int(n2 / n1))
            else: st.append(int(ch))
        return st[0]