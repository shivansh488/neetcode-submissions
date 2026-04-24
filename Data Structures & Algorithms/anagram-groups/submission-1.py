from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for word in strs:
            key = tuple(sorted(word))   # convert word → sorted tuple
            groups[key].append(word)

        return list(groups.values())