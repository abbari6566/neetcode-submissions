class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1]*(len(nums))
        prefix = 1
        for i in range(len(nums)):
            result[i]=prefix
            prefix*=nums[i]
        postfix=1
        for i in range(len(nums)-1,-1,-1):
            result[i] *= postfix
            postfix*=nums[i]
        return result


        #brute force solution below works but O(n^2)
        # result = []
        # for i in nums:
        #     total = 1
        #     for j in nums:
        #         if i!=j:
        #             total *= j
        #     result.append(total)
        # return result





        