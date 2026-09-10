class Solution:
    def rob(self, nums: List[int]) -> int:
        
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0],nums[1])

        #first case -> consider house 1 (nums[0]) and not nums[n-1]
        prev, curr = nums[0], max(nums[0], nums[1])
        for i in range(2,n-1):
            prev, curr = curr, max(prev + nums[i], curr)
        #second case -> consider house 2 -> house n
        prev_, curr_ = nums[1], max(nums[1], nums[2])
        for i in range(3,n):
            prev_, curr_ = curr_ , max(prev_ + nums[i], curr_)
        
        return max(curr, curr_)

#lol it worked somehow!!
#Time - O(n), Space- O(1)
        