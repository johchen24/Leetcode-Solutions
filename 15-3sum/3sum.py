class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []

        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i > 0 and nums[i-1] == nums[i]:
                continue

            low, high = i + 1, len(nums) - 1
            while low < high:
                _sum = nums[i] + nums[low] + nums[high]
                if _sum < 0:
                    low += 1
                elif _sum > 0:
                    high -= 1
                else:
                    ans.append([nums[i], nums[low], nums[high]])
                    low += 1
                    high -= 1
                    while nums[low] == nums[low - 1] and low < high:
                        low += 1
            
        return ans