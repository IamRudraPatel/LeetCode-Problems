class Solution:
    def minimumPushes(self, word: str) -> int:
        A = ord('a')
        freqArr = [0]*26
        for ch in word:
            freqArr[ord(ch)-A] += 1
        freqArr.sort(reverse=True)
        ans = 0
        for i in range(26):
            ans += freqArr[i] * (1 + i//8)
        return ans