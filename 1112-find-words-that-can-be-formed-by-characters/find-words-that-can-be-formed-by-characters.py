class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        freqCh = Counter(chars)
        ans = 0
        
        for word in words:
            freqWord = defaultdict(int)
            good = True
            for ch in word: 
                freqWord[ch] += 1
                if (ch not in freqCh) or (freqCh[ch] < freqWord[ch]):
                    good = False
                    break
            if good: ans += len(word)
        return ans