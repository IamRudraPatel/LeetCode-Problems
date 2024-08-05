class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        mapp = defaultdict(int)
        for st in arr:
            mapp[st] += 1
        for st in mapp:
            if (mapp[st]==1): 
                k -= 1
                if k==0: return st
        return ""