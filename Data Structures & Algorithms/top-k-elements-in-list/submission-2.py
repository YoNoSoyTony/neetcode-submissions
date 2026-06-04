from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 
        frequencyDict = defaultdict(int)
        mostFrequent = 0
        for num in nums:
            frequencyDict[num] += 1
            mostFrequent = max(mostFrequent, frequencyDict[num])

        freqList = [[] for x in range(mostFrequent+1)]
        for num, frequency in frequencyDict.items():
            freqList[frequency].append(num)
        
        kCounter = k
        topK = []

        for index in range(mostFrequent, -1, -1):
            for number in freqList[index]:
                topK.append(number)
                kCounter -= 1
                if kCounter == 0:
                    break
            if kCounter == 0:
                    break
        return topK




        

        