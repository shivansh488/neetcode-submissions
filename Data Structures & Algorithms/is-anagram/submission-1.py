from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_counter1=Counter(s)
        char_counter2=Counter(t)
        return char_counter1==char_counter2
        