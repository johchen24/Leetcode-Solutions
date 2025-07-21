class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        boundaries = [0 for _ in range(n)]

        for i in range(1, n - 1):
            boundaries[i] = max(height[i-1], boundaries[i-1])
        
        postfix = 0
        for j in range(n - 2, -1, -1):
            postfix = max(postfix, height[j+1])
            boundaries[j] = min(boundaries[j], postfix)
        
        water = 0
        for k in range(n):
            water += max(0, boundaries[k] - height[k])
        return water