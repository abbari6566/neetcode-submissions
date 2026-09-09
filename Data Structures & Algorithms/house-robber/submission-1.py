class Solution:
    def rob(self, nums: List[int]) -> int:
        #Bottom Up DP without tabulation so constant space
        #Time - O(n) and space - O(1)
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])

        prev = nums[0]
        curr = max(nums[0],nums[1]) #max profit from house 0 and 1

        for i in range(2,n):
            prev, curr = curr , max(prev+nums[i], curr)
        
        return curr
        