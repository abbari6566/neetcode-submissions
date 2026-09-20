class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        # Array to store all left multiplication
        left = [0] * n
        # Array to store all right multiplication
        right = [0] * n
        
        # Compute prefix products
        left[0] = 1
        for i in range(1, n):
            left[i] = left[i - 1] * nums[i - 1]
            
        # Compute suffix products
        right[n - 1] = 1
        for i in range(n - 2, -1, -1):
            right[i] = right[i + 1] * nums[i + 1]
            
        # Combine left and right products
        ans = [0] * n
        for i in range(n):
            ans[i] = left[i] * right[i]
            
        return ans


        #brute force solution below works but O(n^2)
        # result = []
        # for i in nums:
        #     total = 1
        #     for j in nums:
        #         if i!=j:
        #             total *= j
        #     result.append(total)
        # return result





        