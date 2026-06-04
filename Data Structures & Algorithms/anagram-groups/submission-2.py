from collections import defaultdict
from string import ascii_lowercase as alphabet

class Solution:
    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        keyDict = defaultdict(list)
        for word in strs:
            # create a map of letters and frequency
            alphabet_frequency = defaultdict(int)
            for char in word:
                alphabet_frequency[char] += 1

            # from the alphabet_frequency create a key to store in keyDict
            key = []
            for char in alphabet:
                if char in alphabet_frequency:
                    key.append(f"{char}{alphabet_frequency[char]}")
            key = "".join(key)

            keyDict[key].append(word)
        return list(keyDict.values())



