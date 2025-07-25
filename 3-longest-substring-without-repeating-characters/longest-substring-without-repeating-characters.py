class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right = 0, 0
        seen = set()
        res = 0

        while right < len(s):
            if s[right] in seen:
                while s[left] != s[right]:
                    seen.remove(s[left])
                    left += 1
                left += 1
            else:
                seen.add(s[right])
            res = max(res, len(seen))
            right += 1
        return res

