class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] # always decreasing
        res = [0]*len(temperatures)

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][1]:
                topI, topT = stack.pop()
                res[topI] = i - topI
            stack.append((i, t))
        return res