class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        #difference between each number should be 1
        #check 2 numbers simultaneouslt i and i+1
        nums.sort()
        
        for i in range(len(nums)):
            if nums[i] != i:
                return i
        return len(nums)