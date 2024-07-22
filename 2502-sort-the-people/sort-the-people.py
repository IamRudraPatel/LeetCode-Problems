class Solution:
    def InPlaceMerge(self, heights, names, start, mid, end):
        l: int = start
        r: int = mid + 1
        while l <= mid and r <= end:
            if heights[l] >= heights[r]:
                l = l + 1
            else:
                temp1: int = heights[r]
                temp2: str = names[r]
                idx: int = r
                while idx > l:
                    heights[idx] = heights[idx - 1]
                    names[idx] = names[idx - 1]
                    idx -= 1
                heights[l] = temp1
                names[l] = temp2
                l += 1
                r += 1
                mid += 1
            
    def mergeSort(self, heights, names, start, end):
        if start>=end: return;
        mid: int = (start+end)//2
        self.mergeSort(heights, names, start, mid)
        self.mergeSort(heights, names, mid+1, end)
        self.InPlaceMerge(heights, names, start, mid, end)

    def sortPeople(self, names, heights ) -> list[str]:
        self.mergeSort(heights, names, 0, len(heights)-1)
        return names