from collections import defaultdict
from string import ascii_lowercase


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_s, dict_t = defaultdict(int), defaultdict(int)
        for ch in s:
            dict_s[ch] += 1
        for ch in t:
            dict_t[ch] += 1
        
        for letter in ascii_lowercase:
            if dict_s[letter] != dict_t[letter]:
                return False
        return True