class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0) # add a dummy at the end to make life easier
        stack = []
        maxA = 0

        for i, height in enumerate(heights):
            whereStart = i
            while stack and stack[-1][1] > height:
                topI, topH = stack.pop()
                maxA = max(maxA, topH*(i - topI))
                whereStart = topI
            
            stack.append((whereStart, height))
        
        return maxA