class Solution:
    def minimumPushes(self, word: str) -> int:
        A = ord('a')
        freqArr = [0]*26
        for ch in word:
            freqArr[ord(ch)-A] += 1
        freqArr.sort(reverse=True)
        ans = 0
        for i in range(26):
            ans += freqArr[i]
            if i > 7: ans += freqArr[i]
            if i > 15: ans += freqArr[i]
            if i > 23: ans += freqArr[i]
        return ans