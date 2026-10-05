class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        #brute force
        #difference between each number should be 1
        #check 2 numbers simultaneouslt i and i+1
        # nums.sort()
        
        # for i in range(len(nums)):
        #     if nums[i] != i:
        #         return i
        # return len(nums)
        # nlogn
        result = len(nums)
        for i in range(len(nums)):
            result ^= i ^ nums[i]
        return result

'''
Approach 1. use sum of all natural numbers - sum of all elements in array

Approach 2. Use bitwise XOR to do O(n)

How XOR Works 
Here:
XOR cancels out identical numbers because a ^ a = 0.
Also, a ^ 0 = a.
So if you XOR all numbers from 0 → n and also XOR all elements in the array:

Every number that appears in both gets cancelled.
The only number that doesn’t appear in both (the missing one) remains.
Example:
For nums = [3, 0, 1]:

Indices (0→3): 0 ^ 1 ^ 2 ^ 3 = 0 ^ 1 ^ 2 ^ 3
Array elements: 3 ^ 0 ^ 1
XOR all together → (0 ^ 1 ^ 2 ^ 3) ^ (3 ^ 0 ^ 1)
All common numbers cancel, and what remains is 2.

'''
