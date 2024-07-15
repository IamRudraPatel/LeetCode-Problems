class Solution:
    def countOfAtoms(self, formula: str) -> str:
        n: int = len(formula)
        i: int = 0
        stack: list[{str, int}] = [defaultdict(int)]
        while i < n:
            curCh: str = formula[i]
            if curCh.isupper():
                element: str = curCh
                i += 1
                if (i < n) and (formula[i].islower()):
                    element += formula[i]
                    i += 1
                atomCount: str = ""
                while (i < n) and (formula[i].isdigit()):
                    atomCount += formula[i]
                    i += 1
                atomCount = 1 if not atomCount else int(atomCount)
                stack[-1][element] += atomCount
            elif curCh == "(":
                stack.append(defaultdict(int))
                i += 1
            elif curCh == ")":
                num: str = ""
                i += 1
                while (i < n) and (formula[i].isdigit()):
                    num += formula[i]
                    i += 1
                num = 1 if not num else int(num)
                curMap: defaultdict[str, int] = stack.pop()
                prevMap: defaultdict[str, int] = stack[-1]
                for eles in curMap:
                    prevMap[eles] += curMap[eles] * num
            else: i += 1
        answer: str = ""
        finalMap: defaultdict[str, int] = stack.pop()
        for eles in sorted(finalMap.keys()):
            atomCount = finalMap[eles]
            answer += eles if atomCount == 1 else eles + str(atomCount)
        return answer