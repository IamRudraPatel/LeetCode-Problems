class Solution:
    def reverse(self, arr, low, high):
        while low<=high:
            arr[low], arr[high] = arr[high], arr[low]
            low += 1 
            high -= 1

    def reverseParentheses(self, s: str) -> str:
        answer = []
        skipLen = []
        for ch in s:
            if ch == '(':
                skipLen.append(len(answer))
            elif ch == ')':
                self.reverse(answer, skipLen.pop(), len(answer)-1)
            else: answer.append(ch)
        return "".join(answer)
