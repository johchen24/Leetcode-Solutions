class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = set()

        for i,x in enumerate(nums):
            if i > k:
                seen.remove(nums[i - k - 1])
            if x in seen:
                return True
            seen.add(x)
        return False
        