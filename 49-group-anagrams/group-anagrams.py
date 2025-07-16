class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) # map character count to list of anagrams

        for str in strs:
            count = [0] * 26
            for s in str:
                count[ord(s) - ord('a')] += 1
            res[tuple(count)].append(str)
        return list(res.values())