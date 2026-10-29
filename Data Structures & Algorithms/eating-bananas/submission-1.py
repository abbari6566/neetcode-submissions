import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def valid_k(k):

            hours = 0

            for p in piles:
                hours += math.ceil(p/k)

            return hours <= h
        
        minSpeed = 1
        maxSpeed = max(piles)
        
        while minSpeed < maxSpeed:

            k = (minSpeed + maxSpeed) // 2

            if valid_k(k):
                maxSpeed = k
            else:
                minSpeed = k + 1
        
        return maxSpeed

# Time - O(n * log n)
# Each serch does array iteration that is n
# Binary Search is log n
# so overall becomes n*logn

        