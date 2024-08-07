class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0: return "Zero"

        onesMap = {1: "One",
                   2: "Two",
                   3: "Three",
                   4: "Four",
                   5: "Five",
                   6: "Six",
                   7: "Seven",
                   8: "Eight",
                   9: "Nine",
                   10: "Ten",
                   11: "Eleven",
                   12: "Twelve",
                   13: "Thirteen",
                   14: "Fourteen",
                   15: "Fifteen",
                   16: "Sixteen",
                   17: "Seventeen",
                   18: "Eighteen",
                   19: "Nineteen"}

        tensMap = {2: "Twenty",
                   3: "Thirty",
                   4: "Forty",
                   5: "Fifty",
                   6: "Sixty",
                   7: "Seventy",
                   8: "Eighty",
                   9: "Ninety"}

        def helper(n: int) -> str:
            s = []
            hundreds = n // 100
            if hundreds:
                s.append(onesMap[hundreds] + " Hundred")
            last2 = n % 100
            if last2 >= 20: 
                tens, ones = last2 // 10, last2 % 10
                s.append(tensMap[tens])
                if ones: 
                    s.append(onesMap[ones])
            elif last2: 
                s.append(onesMap[last2])
            return " ".join(s)
        
        places = ["", " Thousand", " Million", " Billion"]
        i = 0
        ans = []
        while num:
            threedigit = num % 1000
            s = helper(threedigit)
            print(s)
            if s:
                ans.append(s + places[i])
            num = num // 1000
            i += 1
        ans.reverse()
        return " ".join(ans)