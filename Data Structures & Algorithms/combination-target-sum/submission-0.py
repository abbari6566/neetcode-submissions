class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res,sol = [],[]
        n = len(nums)

        def backtrack(i, cur_sum):
            if cur_sum == target:
                res.append(sol[:])
                return
            if cur_sum > target or i==n:
                return
            
            backtrack(i+1, cur_sum) #go to next index dont use anymore of this

            sol.append(nums[i]) #use this number
            backtrack(i, cur_sum + nums[i]) #use the same number again creating duplicate
            sol.pop()
        
        backtrack(0,0)
        return res
        #Time: O(n**t), Space: O(N) roughly
        