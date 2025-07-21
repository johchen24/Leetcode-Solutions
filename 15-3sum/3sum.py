class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()

        for i in range(0, len(nums) - 2):
            if nums[i] > 0:
                break
            if i > 0 and nums[i-1] == nums[i]:
                continue
            
            left = i + 1
            right = len(nums) - 1
            while left < right:
                summ = nums[i] + nums[left] + nums[right]
                if summ == 0:
                    ans.append([nums[i], nums[left], nums[right]])
                    left += 1 
                    right -= 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
                    while nums[right] == nums[right + 1] and left < right:
                        right -= 1
                if summ < 0:
                    left += 1
                if summ > 0:
                    right -= 1
        return ans
