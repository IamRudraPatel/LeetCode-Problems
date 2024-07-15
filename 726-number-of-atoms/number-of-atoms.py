class Solution:
    def countOfAtoms(self, formula: str) -> str:
        n: int = len(formula)
        i: int = 0
        stack: list = [defaultdict(int)]
        while i < n:
            curCh = formula[i]
            if curCh == '(':
                stack.append(defaultdict(int))
                i+=1
            elif curCh == ')':
                num = ""
                i += 1
                while (i<n) and (formula[i].isdigit()):
                    num += formula[i]
                    i += 1
                num = 1 if not num else int(num)
                curMap = stack.pop()
                prevMap = stack[-1]
                for eles in curMap:
                    prevMap[eles] += curMap[eles] * num
            elif curCh.isupper(): 
                element = curCh
                atomCount = ""
                i += 1
                if (i<n) and (formula[i].islower()):
                    element += formula[i]
                    i += 1 
                while (i<n) and (formula[i].isdigit()):
                    atomCount += formula[i]
                    i += 1
                atomCount = 1 if not atomCount else int(atomCount)
                stack[-1][element] += atomCount
        answer = ""
        finalMap = stack.pop()
        for eles in sorted(finalMap.keys()):
            atomCount = finalMap[eles]
            answer += eles if atomCount == 1 else eles + str(atomCount)
        return answer