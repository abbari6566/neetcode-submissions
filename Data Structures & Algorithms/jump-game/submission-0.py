class Solution:
    def canJump(self, nums: List[int]) -> bool:
        #goal is the last element at first
        goal = len(nums)-1
        for i in range(len(nums)-1,-1,-1):
            if i+nums[i]>=goal:
                goal=i
        return goal == 0
#time - O(n)

        