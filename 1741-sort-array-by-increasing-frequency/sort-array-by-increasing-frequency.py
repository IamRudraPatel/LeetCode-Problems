class Solution:
    def frequencySort(self, arr: List[int]) -> List[int]:
        count = Counter(arr)
        arr.sort(key=lambda x: (count[x], -x))
        return arr
