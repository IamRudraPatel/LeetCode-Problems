class Solution:
    def largestGoodInteger(self, num: str) -> str:
        com = ""
        ans = ""
        for i in range(len(num)-2):
            if num[i] == num[i+1] == num[i+2]:
                com = max(com, num[i])
                ans = com * 3
        return ans