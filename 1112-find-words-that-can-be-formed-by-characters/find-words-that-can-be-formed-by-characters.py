class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        freqCh = defaultdict(int)
        for ch in chars: freqCh[ch] += 1
        ans = 0
        for word in words:
            freqWord = defaultdict(int)
            for ch in word: freqWord[ch] += 1
            for ch in freqWord:
                if freqCh[ch] < freqWord[ch]: break
            else: ans += len(word)
        return ans