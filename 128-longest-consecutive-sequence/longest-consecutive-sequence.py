class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)

        ans = 0
        for x in numsSet:
            if x - 1 not in numsSet:
                count = 1
                while x + count in numsSet:
                    count +=1
                ans = max(ans, count)
        return ans