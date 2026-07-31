
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        
        freq = [[] for i in range(len(nums) + 1)]
        
        for n in nums:
            # Key is the number

            # Value is the number of times it repeats in nums
            count[n] = 1 + count.get(n, 0)
        
        for key, value in count.items():
            # Freq's value index represents the number in nums that repeats
            # value number of times from 0 to len(nums)            
            freq[value].append(key)
        
        res = []

        for i in range(len(freq)-1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
        
        return res