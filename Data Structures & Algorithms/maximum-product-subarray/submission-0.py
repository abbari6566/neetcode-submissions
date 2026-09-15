class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        cur_max, cur_min = nums[0], nums[0]
        result = nums[0]

        for i in range (1, len(nums)):
            temp = cur_min
            cur_min = min(nums[i], temp*nums[i], cur_max*nums[i])
            cur_max = max(nums[i], temp*nums[i], cur_max*nums[i])
            result = max(cur_max, result)

        return result

#Time - O(n)    