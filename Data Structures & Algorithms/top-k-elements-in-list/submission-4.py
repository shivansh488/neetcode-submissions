import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dick=Counter(nums)
        return heapq.nlargest(k,dick.keys(),key=dick.get)