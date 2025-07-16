class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMapIndex = {}

        for i, num in enumerate(nums):
            if target - num in numMapIndex:
                return [i, numMapIndex[target-num]]
            else:
                numMapIndex[num]=i
        
        