class Solution:
    def countOfAtoms(self, formula: str) -> str:
        n: int = len(formula)
        i: int = 0
        stack: list = [defaultdict(int)]
        while i < n:
            curCh = formula[i]
            if curCh == '(':
                stack.append(defaultdict(int))
            elif curCh == ')':
                num = ""
                while (i+1)<n and (formula[i+1].isdigit()):
                    num += formula[i+1]
                    i += 1
                num = 1 if not num else int(num)
                curMap = stack.pop()
                prevMap = stack[-1]
                for eles in curMap:
                    prevMap[eles] += curMap[eles] * num
            elif curCh.isupper(): 
                element = curCh
                atomCount = ""
                if (i+1)<n and (formula[i+1].islower()):
                    element += formula[i+1] 
                    i += 1 
                while (i+1)<n and (formula[i+1].isdigit()):
                    atomCount += formula[i+1]
                    i += 1
                atomCount = 1 if not atomCount else int(atomCount)
                stack[-1][element] += atomCount
            i += 1
        answer = ""
        finalMap = stack.pop()
        for eles in sorted(finalMap.keys()):
            atomCount = finalMap[eles]
            answer += eles if atomCount == 1 else eles + str(atomCount)
        return answer