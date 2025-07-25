class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        charCount = {}
        
        left, right = 0, 0
        maxFrequency = 0
        while right < len(s):
            charCount[s[right]] = charCount.get(s[right], 0) + 1
            maxFrequency = max(maxFrequency, charCount[s[right]])

            while (right - left + 1) - maxFrequency > k:
                charCount[s[left]] -= 1
                left += 1
            res = max(res, right - left + 1)
            right += 1
        return res