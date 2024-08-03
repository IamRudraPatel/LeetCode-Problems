class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        count = defaultdict(int)
        for i in range(len(target)):
            count[target[i]] += 1
            count[arr[i]] -= 1
        for n in count:
            if count[n] != 0: return False
        return True