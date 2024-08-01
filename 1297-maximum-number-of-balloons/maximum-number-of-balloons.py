class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        countMap = defaultdict(int)
        for ch in text: 
            countMap[ch] += 1
        return min(countMap['b'], countMap['a'], countMap['l']//2, countMap['o']//2, countMap['n'])
