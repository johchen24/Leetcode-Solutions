class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        myset = set()
        for x in nums:
            if x in myset:
                return True
            myset.add(x)
        return False
        