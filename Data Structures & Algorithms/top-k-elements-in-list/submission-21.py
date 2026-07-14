from collections import deque
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = {}
        freqK = [[] for buckets in range(len(nums)+1)]

        for num in nums:
            count[num] = count.get(num, 0) + 1

        for number, count in count.items():
            freqK[count].append(number)

        result = []
        for i in range(len(freqK)-1, 0, -1):
            for each_bucket in freqK[i]:
                result.append(each_bucket)
                if len(result) == k:
                    return result



        

        
            




        