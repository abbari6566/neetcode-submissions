class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #brute force double for loop
        # max_sum = float('-inf')
        # for i in range(len(nums)):
        #     cur_sum = 0
        #     for j in range(i, len(nums)):
        #         cur_sum += nums[j]
        #         max_sum = max(max_sum, cur_sum)
        # return max_sum 
        #passes 21/22 cases, needs optimization from O(n^2) 
        result = nums[0]
        maxEndingSum = nums[0]
        for i in range(1,len(nums)):
            maxEndingSum = max(maxEndingSum + nums[i],nums[i])
            result = max(result, maxEndingSum)
        return result
                     
        