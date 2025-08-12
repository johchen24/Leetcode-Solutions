class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high = 1, max(piles)
        ans = high
        
        while low <= high:
            mid = (low + high) // 2
            total = 0
            for pile in piles:
                total += math.ceil(pile/mid)
            if total <= h:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans