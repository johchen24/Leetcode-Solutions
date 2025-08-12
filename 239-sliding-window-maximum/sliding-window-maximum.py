class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # always decreasing deque
        ans = []
        dq = deque()
        left, right = 0, 0

        while right < k - 1:
            while dq and dq[-1] < nums[right]:
                dq.pop()
            dq.append(nums[right])
            right += 1

        while right < len(nums):
            while dq and dq[-1] < nums[right]:
                dq.pop()
            dq.append(nums[right])

            ans.append(dq[0])

            if nums[left] == dq[0]:
                dq.popleft()
            left += 1
            right += 1
        return ans
