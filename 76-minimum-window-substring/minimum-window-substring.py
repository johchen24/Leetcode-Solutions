class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t) or not t or not s:
            return ""

        shortest = ""
        shortestLen = len(s) + 1


        # track characters in t, want everything to match
        countT = collections.Counter(t)
        wantLen = len(countT)

        # use defaultdict to track window
        countS = defaultdict(int)
        left, right = 0, 0

        # sliding window the rest
        while right < len(s):
            c = s[right]
            countS[c] += 1

            # increase matches
            if countT[c] != 0 and countS[c] == countT[c]:
                wantLen -= 1
                
            # try closing in the left
            while wantLen == 0:
                if right - left + 1 < shortestLen:
                    shortestLen = right - left + 1
                    shortest = s[left:right + 1]
                    if shortestLen == len(t):
                        return shortest

                remove = s[left]
                countS[remove] -= 1
                if countT[remove] and countS[remove] < countT[remove]:
                    wantLen += 1
                left += 1
            right += 1              
        return shortest