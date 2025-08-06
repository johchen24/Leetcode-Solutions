class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False

        count1, count2 = [0]*26, [0]*26
        for i in range(len(s1)):
            count1[ord(s1[i]) - ord('a')] += 1
            count2[ord(s2[i]) - ord('a')] += 1

        numMatches = 0 # need all 26 letters count to match
        for i in range(26):
            if count1[i] == count2[i]: numMatches += 1
        
        left, right = 0, len(s1)

        while right < len(s2):
            if numMatches == 26: return True

            ind = ord(s2[right]) - ord('a')
            count2[ind] += 1
            if count1[ind] == count2[ind]:
                numMatches += 1
            elif count1[ind] + 1 == count2[ind]:
                numMatches -= 1
            

            ind = ord(s2[left]) - ord('a')
            count2[ind] -= 1
            if count1[ind] == count2[ind]:
                numMatches += 1
            elif count1[ind] - 1 == count2[ind]:
                numMatches -= 1

            left += 1
            right += 1
        return numMatches == 26