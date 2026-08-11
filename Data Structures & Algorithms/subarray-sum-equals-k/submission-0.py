class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        result = 0
        curSum = 0
        prefixSum = {0:1} #0 is for prefix sum before idx 0 element
        for n in nums:
            curSum+=n
            prevSum = curSum - k
            result += prefixSum.get(prevSum,0)
            prefixSum[curSum]=1+prefixSum.get(curSum,0)
        return result
'''
Time Complexiy
- O(N) for n times in loop
'''
        