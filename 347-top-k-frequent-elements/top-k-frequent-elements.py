class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # bucket sort
        freq = [[] for i in range(len(nums) + 1)]

        for n, c in collections.Counter(nums).items():
            freq[c].append(n)

        ans = []
        for i in range(len(nums), 0, -1):
            for n in freq[i]:
                ans.append(n)
                if len(ans) == k: 
                    return ans