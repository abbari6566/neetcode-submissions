class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        sortedArr = sorted(zip(position, speed), reverse = True)
        stack = []

        for p, s in sortedArr:

            timeLeft = (target - p) / s

            if not stack or timeLeft > stack[-1]:
                stack.append(timeLeft)
        
        return len(stack)

'''
Time: 
sort - O(nlogn)
iterate over the array - O(n)
overall - O(n + nlogn) -> O(n log n)

Space:
sortedArr and stack - O(n)
'''
