class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        prefixSum = 0
        prefixMap = {0:1} #0 is for prefix sum before idx 0 element

        for n in nums:

            prefixSum+=n

            if prefixSum - k in prefixMap: 
                #if the preixSum exist get its frquency (value in dict)
                count += prefixMap[prefixSum - k]
            
            prefixMap[prefixSum] = 1 + prefixMap.get(prefixSum,0)

        return count
'''
Time Complexiy
- O(N) for n times in loop
'''
        