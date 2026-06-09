class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #brute force is O(n^2)
        #lets use hashmaps
        hashmap = {}
        n = len(nums)
        #add each element to the map
        for i in range(n):
            hashmap[nums[i]] = i
        for i in range(n):
            compare = target - nums[i]
            if compare in hashmap and hashmap[compare] != i:
                return [i, hashmap[compare]]
        
        