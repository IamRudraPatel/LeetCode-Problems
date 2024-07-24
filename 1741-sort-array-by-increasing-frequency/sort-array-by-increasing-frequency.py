class Solution:
    def frequencySort(self, arr: List[int]) -> List[int]:
        count = Counter(arr).most_common()
        count.sort(key=lambda x: (x[1], -x[0]))
        ans = []
        for i in count:
            ans += ([i[0]]*i[1])
        return ans