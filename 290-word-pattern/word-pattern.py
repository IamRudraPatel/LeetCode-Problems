class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(' ')
        n = len(pattern)
        if n!=len(words): return False
        chToWord = {}
        wordToCh = {}
        for i in range(n):
            ch, word = pattern[i], words[i]
            if (ch in chToWord) and (chToWord[ch]!=word): return False
            if (word in wordToCh) and (wordToCh[word]!=ch): return False
            chToWord[ch] = word
            wordToCh[word] = ch
        return True
