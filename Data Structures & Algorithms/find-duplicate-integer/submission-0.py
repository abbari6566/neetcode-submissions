from collections import Counter

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        hashmap = {}

        for n in nums:
            if n not in hashmap:
                hashmap[n] = 1
            hashmap[n] += 1
        
        return max(hashmap, key=hashmap.get)