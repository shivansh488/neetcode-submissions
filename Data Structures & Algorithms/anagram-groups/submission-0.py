class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            count = [0] * 26  # to count letters a–z,
            for c in s:
                count[ord(c) - ord('a')] += 1 #position nikalnae ke liye or phir character ka count rakhnae ke liye
            res[tuple(count)].append(s) #agar do count same hai to unkae do anagrams hongae
        return list(res.values())