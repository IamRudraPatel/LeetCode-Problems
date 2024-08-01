class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        ballMap = {'b': 1, 'a': 1, 'l': 2, 'o': 2, 'n': 1}
        countMap = {}
        for ch in text:
            countMap[ch] = countMap.get(ch, 0) + 1
        ans = len(text)
        for ch in ballMap:
            count = countMap.get(ch, 0)//ballMap[ch]
            if count == 0: return 0
            else: ans = min(count, ans)
        return ans