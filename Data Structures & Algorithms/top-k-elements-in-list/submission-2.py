import heapq
from collections import Counter
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)

        # get top k keys based on frequency
        result = heapq.nlargest(k, freq.keys(), key=freq.get)

        return result ##imppppp