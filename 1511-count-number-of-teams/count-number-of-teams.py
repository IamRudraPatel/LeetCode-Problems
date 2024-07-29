class Solution:
    def numTeams(self, rating: List[int]) -> int:
        ans = 0
        n = len(rating)
        for m in range(1, n-1):
            midVal, leftSmal, rightLarg = rating[m], 0, 0
            for i in range(m):
                if rating[i] < midVal:
                    leftSmal += 1
            for j in range(m+1, n):
                if rating[j] > midVal:
                    rightLarg += 1
            ans += leftSmal * rightLarg
            leftLarg = m - leftSmal
            rightSmal = n - 1 - m - rightLarg
            ans += leftLarg * rightSmal
        return ans