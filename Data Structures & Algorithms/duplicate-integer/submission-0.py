class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash_map = set()
        for n in nums:
            if n not in hash_map:
                hash_map.add(n)
            else:
                return True
        #if it exits the loop with returning True, means no dup
        return False

#time -> O(n)
        